from entidade.cartao_de_credito import CartaoDeCredito
from limite.tela_cartao_de_credito import TelaCartaoDeCredito


class ControladorCartaodeCredito:
    def __init__(self):
        self.__tela_cartao_de_credito = TelaCartaoDeCredito()
        self.__usuario = None
        self.__continua_nesse_menu = True

    def definir_usuario(self, usuario):
        self.__usuario = usuario

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_cartao, 2: self.alterar_cartao, 3: self.remover_cartao,
                        4: self.retornar_cartao, 0: self.retorna}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_cartao_de_credito.open()]()

    def cadastrar_cartao(self):
        if self.__usuario.cartao is None:
            dados_cartao = self.__tela_cartao_de_credito.cadastra_cartao()
            cartao = CartaoDeCredito(dados_cartao["nome portador"], dados_cartao["instituicao"],
                                     dados_cartao["numero cartao"], dados_cartao["validade"],
                                     dados_cartao["codigo seguranca"])
            self.__usuario.cartao = cartao
        else:
            self.__tela_cartao_de_credito.show_message("Aviso!", "O usuario jah possui um cartao cadastrado!")

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
            self.__usuario.cartao = None
        else:
            self.__tela_cartao_de_credito.show_message("Aviso!", "O usuario nao possui um cartao cadastrado!")

    def retornar_cartao(self):
        if self.__usuario.cartao is not None:
            self.__tela_cartao_de_credito.mostra_cartao({"nome": self.__usuario.cartao.nome_portador,
                                                         "instituicao": self.__usuario.cartao.instituicao,
                                                         "numero": self.__usuario.cartao.numero,
                                                         "validade": self.__usuario.cartao.validade,
                                                         "codigo": self.__usuario.cartao.codigo_seguranca})
        else:
            self.__tela_cartao_de_credito.show_message("Aviso!", "O usuario nao possui um cartao cadastrado!")

    def retorna(self):
        self.__continua_nesse_menu = False
