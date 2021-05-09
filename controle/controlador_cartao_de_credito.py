from entidade.cartao_de_credito import CartaoDeCredito
from limite.tela_cartao_de_credito import TelaCartaoDeCredito
from limite.tela_cartao_cadastra import TelaCartaoCadastra
from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.numero_cartao_invalido_exception import NumeroCartaoInvalidoException
from excecoes.validade_invalida_exception import ValidadeInvalidaException
import string


class ControladorCartaodeCredito:
    def __init__(self):
        self.__tela_cartao_de_credito = TelaCartaoDeCredito()
        self.__tela_cartao_cadastra = TelaCartaoCadastra()
        self.__usuario = None
        self.__continua_nesse_menu = True

    def definir_usuario(self, usuario):
        self.__usuario = usuario

    def abre_tela(self, usuario):
        self.definir_usuario(usuario)
        lista_opcoes = {1: self.cadastrar_cartao, 2: self.alterar_cartao, 3: self.remover_cartao,
                        4: self.retornar_cartao, 0: self.retorna}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_cartao_de_credito.open()]()
            self.__tela_cartao_de_credito.close()

    def cadastrar_cartao(self):
        if self.__usuario.cartao is not None:
            self.__tela_cartao_de_credito.show_message("Aviso", "Este usuario jah possui "
                                                       "um cartao cadastrado!")
        else:
            while True:
                dados_cartao = self.__tela_cartao_cadastra.open()
                if dados_cartao[0] == "Enviar":
                    try:
                        print(dados_cartao)
                        print(dados_cartao[1]['nome_portador'], dados_cartao[1]['numero'], dados_cartao[1]['codigo'])
                        if dados_cartao[1]['nome_portador'] != self.__usuario.nome:
                            raise NomeInvalidoException
                        if not 13 < len(dados_cartao[1]['numero']) < 16:
                            raise NumeroCartaoInvalidoException
                        for digito in dados_cartao[1]['numero']:
                            if digito not in string.digits:
                                raise NumeroCartaoInvalidoException
                        if len(dados_cartao[1]['codigo']) != 3:
                            raise NumeroCartaoInvalidoException
                        if dados_cartao[1]['data_validade'] is None:
                            raise ValidadeInvalidaException
                        data_de_validade = dados_cartao[1]['data_validade'].split(" ")
                        self.__usuario.add_cartao(dados_cartao[1]['nome_portador'], dados_cartao[1]['bandeira'][0],
                                                dados_cartao[1]['numero'], data_de_validade[0],
                                                dados_cartao[1]['codigo'])
                        self.__tela_cartao_cadastra.close()
                        break

                    except NumeroCartaoInvalidoException as e:
                        self.__tela_cartao_de_credito.show_message("Aviso", str(e))
                        self.__tela_cartao_cadastra.close()
                        break
                    except ValidadeInvalidaException as e:
                        self.__tela_cartao_de_credito.show_message("Aviso", str(e))
                        self.__tela_cartao_cadastra.close()
                        break

    def alterar_cartao(self):
        if self.__usuario.cartao is not None:
            dados = self.__tela_cartao_de_credito.altera_cartao()
            self.__usuario.cartao.nome_portador = dados["nome portador"]
            self.__usuario.cartao.instituicao = dados["instituicao"]
            self.__usuario.cartao.numero = dados["numero cartao"]
            self.__usuario.cartao.validade = dados["validade"]
            self.__usuario.cartao.codigo_seguranca = dados["codigo seguranca"]
        else:
            self.__tela_cartao_de_credito.show_message("Aviso!", "O usuario nao possui um cartao cadastrado!")

    def remover_cartao(self):
        if self.__usuario.cartao is not None:
            self.__usuario.remover_cartao()
        else:
            self.__tela_cartao_de_credito.show_message("Aviso!", "O usuario nao possui um cartao cadastrado!")

    def retornar_cartao(self):
        if self.__usuario.cartao is None:
            self.__tela_cartao_de_credito.show_message("Aviso!", "O usuario nao possui "
                                                       "um cartao cadastrado!")
        else:
            self.__tela_cartao_de_credito.show_message("Seu cartao de credito", "Titular: " +
                                                                                self.__usuario.cartao.nome_portador +
                                                                                "\nInstituicao: " + self.__usuario.cartao.instituicao
                                                                                + "\nNumero: " + self.__usuario.cartao.numero
                                                                                + "\nValidade: " + self.__usuario.cartao.validade
                                                                                + "\nCodigo de seguranca: " +
                                                                                self.__usuario.cartao.codigo_seguranca)
            
            self.__tela_cartao_de_credito.mostra_cartao({"nome": self.__usuario.cartao.nome_portador,
                                                         "instituicao": self.__usuario.cartao.instituicao,
                                                         "numero": self.__usuario.cartao.numero,
                                                         "validade": self.__usuario.cartao.validade,
                                                         "codigo": self.__usuario.cartao.codigo_seguranca})

    def retorna(self):
        self.__continua_nesse_menu = False


