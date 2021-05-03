from entidade.jogo import Jogo
from limite.tela_jogo import TelaJogo
from limite.tela_jogo_nome import TelaJogoNome
from limite.tela_jogo_cadastro import TelaJogoCadastro
from limite.tela_jogo_alterar import TelaJogoAlterar
from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.genero_invalido_exception import GeneroInvalidoException
from excecoes.desenvolvedora_invalida_exception import DesenvolvedoraInvalidaException


class ControladorJogo:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogo = TelaJogo()
        self.__tela_jogo_nome = TelaJogoNome()
        self.__tela_jogo_cadastro = TelaJogoCadastro()
        self.__tela_jogo_alterar = TelaJogoAlterar()
        self.__jogos = []
        self.__continua_nesse_menu = True
        self.__desenvolvedoras = None
        self.__compras = None

    def gerar_desenvolvedoras_e_compras(self, desenvolvedoras, compras):
        self.__desenvolvedoras = desenvolvedoras
        self.__compras = compras

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_jogo, 2: self.altera_jogo, 3: self.get_dados_jogo,
                        4: self.lista_jogos, 5: self.remover_jogo, 0: self.voltar}
        self.__continua_nesse_menu = True

        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_jogo.open()]()
            self.__tela_jogo.close()

    def cadastra_jogo(self):
        if len(self.__desenvolvedoras) == 0:
            self.__tela_jogo.show_message("Aviso!", "Não existem desenvolvedoras "
                                                    "disponiveis! Por favor insira pelo "
                                                    "menos uma antes de cadastrar um jogo ")
        else:
            while True:
                dados_jogo = self.__tela_jogo_cadastro.open(self.nomes_desenvolvedoras())
                if dados_jogo[0] == 'Submit':
                    try:
                        if len(dados_jogo[1][0]) == 0:
                            raise NomeInvalidoException
                        if len(dados_jogo[1][2]) == 0:
                            raise GeneroInvalidoException
                        if len(dados_jogo[1][1]) == 0 or dados_jogo[1][1] not in self.nomes_desenvolvedoras():
                            raise DesenvolvedoraInvalidaException
                        for jogo in self.__jogos:
                            if jogo.nome == dados_jogo[1][0]:
                                raise NomeInvalidoException
                        if float(dados_jogo[1][4]) > 1500 or float(dados_jogo[1][4]) < 0:
                            raise ValueError
                        for desenvolvedora in self.__desenvolvedoras:
                            if desenvolvedora.nome == dados_jogo[1][1]:
                                jogo = Jogo(dados_jogo[1][0], desenvolvedora, dados_jogo[1][2], int(dados_jogo[1][3]),
                                            float(dados_jogo[1][4]))
                                self.__jogos.append(jogo)
                                desenvolvedora.incluir_jogo(jogo)
                                self.__tela_jogo_cadastro.close()
                                break
                        break
                    except NomeInvalidoException as e:
                        self.__tela_jogo.show_message("Aviso", str(e))

                    except ValueError:
                        self.__tela_jogo.show_message("Aviso", "Valor invalido para o preço! (0 ate 1500)")

                    except GeneroInvalidoException as e:
                        self.__tela_jogo.show_message("Aviso", str(e))

                    except DesenvolvedoraInvalidaException as e:
                        self.__tela_jogo.show_message("Aviso", str(e))
                else:
                    self.__tela_jogo.show_message("Aviso", "Processo Cancelado")
                    break

    def lista_jogos(self):
        if len(self.__jogos) == 0:
            self.__tela_jogo.show_message("Aviso!", "Não existem jogos disponiveis! "
                                                    "Por favor insira pelo menos um")
        else:
            lista_jogos = list()
            for jogo in self.__jogos:
                lista_jogos.append("\nNome do Jogo: " + jogo.nome + "\nDesenvolvedora do jogo: " +
                                   jogo.desenvolvedora.nome + "\nGenero do jogo: " + jogo.genero +
                                   "\nFaixa etaria do jogo: " + str(jogo.faixa_etaria) + "\nPreço do jogo: " +
                                   str(jogo.preco))
            self.__tela_jogo.show_message("Listagem de Jogos", "\n".join(lista_jogos))

    def altera_jogo(self):
        if len(self.__jogos) == 0:
            self.__tela_jogo.show_message("Aviso!", "Não existem jogos disponiveis! "
                                                    "Por favor insira pelo menos um")
        else:
            jogo = self.get_jogo_by_nome()
            if jogo is not None:
                nome_antigo = jogo.nome
                while True:
                    try:
                        dados_jogo = self.__tela_jogo_alterar.open(self.nomes_desenvolvedoras())
                        if dados_jogo is not None:
                            if dados_jogo[1][0] in self.nomes_jogo() and dados_jogo[1][0] != nome_antigo:
                                raise NomeInvalidoException
                            if float(dados_jogo[1][4]) > 1500 or float(dados_jogo[1][4]) < 0:
                                raise ValueError
                            break
                        else:
                            self.__tela_jogo.show_message("Aviso", "Processo Cancelado")
                            break
                    except NomeInvalidoException as e:
                        self.__tela_jogo.show_message("Aviso", str(e))

                    except ValueError:
                        self.__tela_jogo.show_message("Aviso", "Valor invalido para o preço! (0 ate 1500)")

                if dados_jogo is not None:
                    jogo.nome = dados_jogo[1][0]
                    jogo.genero = dados_jogo[1][2]
                    jogo.preco = dados_jogo[1][3]
                    jogo.faixa_etaria = dados_jogo[1][4]
                    if dados_jogo[1][1] != jogo.desenvolvedora.nome:
                        for desenvolvedora in self.__desenvolvedoras:
                            if desenvolvedora == jogo.desenvolvedora:
                                desenvolvedora.excluir_jogo(jogo)
                            elif dados_jogo[1][1] == desenvolvedora.nome:
                                desenvolvedora.incluir_jogo(jogo)
                                jogo.desenvolvedora = desenvolvedora

    def get_dados_jogo(self):
        if len(self.__jogos) == 0:
            self.__tela_jogo.show_message("Aviso!", "Não existem jogos disponiveis! "
                                                    "Por favor insira pelo menos um")
        else:
            jogo = self.get_jogo_by_nome()
            if jogo is not None:
                self.__tela_jogo.show_message(jogo.nome.upper(), "Nome do Jogo: " + jogo.nome +
                                              "\nDesenvolvedora do jogo: " + jogo.desenvolvedora.nome +
                                              "\nGenero do jogo: " + jogo.genero + "\nFaixa etaria do jogo: " +
                                              str(jogo.faixa_etaria) + "\nPreço do jogo: " + str(jogo.preco))

    def remover_jogo(self):
        if len(self.__jogos) == 0:
            self.__tela_jogo.show_message("Aviso!", "Não existem jogos disponiveis! "
                                                    "Por favor insira pelo menos um")
        else:
            jogo = self.get_jogo_by_nome()
            if jogo is not None:
                jogo.desenvolvedora.excluir_jogo(jogo)
                for compra in jogo.compras:
                    compra.usuario.remover_compra(compra)
                    compra.usuario.remover_jogo(jogo)
                for compra in self.__compras:
                    if compra.jogo == jogo:
                        self.__compras.remove(compra)
                self.__jogos.remove(jogo)
                self.__tela_jogo.show_message("Sucesso", "Jogo removido com sucesso")

    def voltar(self):
        self.__continua_nesse_menu = False

    def get_jogo_by_nome(self):
        if len(self.__jogos) == 0:
            self.__tela_jogo.show_message("Aviso!", "Não existem jogos disponiveis! "
                                                    "Por favor insira pelo menos um")
        else:
            while True:
                try:
                    nome = self.__tela_jogo_nome.open(self.nomes_jogo())
                    if nome[0] == 'Submit':
                        for jogo in self.__jogos:
                            if jogo.nome == nome[1][0]:
                                self.__tela_jogo_nome.close()
                                return jogo
                        raise NomeInvalidoException
                    else:
                        self.__tela_jogo_nome.show_message('Aviso', 'Processo Cancelado')
                        self.__tela_jogo_nome.close()
                        return None
                except NomeInvalidoException as e:
                    self.__tela_jogo.show_message('Aviso', str(e))
                    self.__tela_jogo_nome.close()

    @property
    def jogos(self):
        return self.__jogos

    def nomes_jogo(self):
        jogos = []
        for jogo in self.__jogos:
            jogos.append(jogo.nome)
        return jogos

    def nomes_desenvolvedoras(self):
        desenvolvedoras = []
        for desenvolvedora in self.__desenvolvedoras:
            desenvolvedoras.append(desenvolvedora.nome)

        return desenvolvedoras
