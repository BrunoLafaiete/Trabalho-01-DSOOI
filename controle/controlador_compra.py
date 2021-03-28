from limite.tela_compra import TelaCompra
from entidade.compra import Compra

class ControladorCompra:
    def __init__(self, controlador_sistema):
        self.__compras = []
        self.tela_compra = TelaCompra()
        self.__controlador_sistema = controlador_sistema
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {1: self.verifica_dados_compra, 0: self.retorna_menu_principal}
        self.__continua_nesse_menu = True
        if self.__continua_nesse_menu:
            lista_opcoes[self.tela_compra.tela_opcoes()]()

    def efetua_compra(self):
        pass

    def verifica_dados_compra(self):
        informacoes_compra = self.tela_compra.verifica_compra()
        for compra in self.__compras:
            if compra.usuario.email == informacoes_compra["email"]:
                if compra.usuario.senha == informacoes_compra["senha"]:
                    if compra.identificador == informacoes_compra["identificador"]:
                        self.tela_compra.retorna_informacoes_compra({"jogo": compra.jogo.nome, "usuario": compra.usuario.nome, "data": compra.data})

    def retorna_menu_principal(self):
        self.__continua_nesse_menu = False