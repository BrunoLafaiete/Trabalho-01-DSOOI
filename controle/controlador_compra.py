from limite.tela_compra import TelaCompra
from entidade.compra import Compra

class ControladorCompra:
    def __init__(self, controlador_sistema):
        self.__compras = []
        self.__tela_compra = TelaCompra()
        self.__controlador_sistema = controlador_sistema
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {1: self.comprar_jogo, 2: self.verifica_dados_compra, 3: self.historico_compras_usuario, 0: self.retorna_menu_principal}
        self.__continua_nesse_menu = True
        if self.__continua_nesse_menu:
            lista_opcoes[self.__tela_compra.tela_opcoes()]()

    def comprar_jogo(self):
        dados_compra = self.__tela_compra.compra_by_name()
        for usuario in self.__controlador_sistema.controlador_usuario.usuarios:
            if usuario.email == dados_compra["email"]:
                if usuario.jogos.nome == dados_compra["jogo"]:
                    for jogo in self.__controlador_sistema.controlador_jogo.jogos:
                        if jogo.nome == dados_compra["jogo"]:
                            compra = Compra(jogo, usuario)
                            self.__compras.append(compra)
                            usuario.saldo -= jogo.preco

    def historico_compras_usuario(self):
        email = self.__tela_compra.historico_compras()
        for usuario in self.__controlador_sistema.controlador_usuario.usuarios:
            if usuario.email == email:
                for compra in usuario.compras:
                    self.__tela_compra.retorna_historico_compras({"nome": compra.jogo.nome, "preco": compra.jogo.preco, "desenvolvedora": compra.jogo.desenvolvedora.nome,
                                                                  "faixa_etaria": compra.jogo.faixa_etaria, "genero": compra.jogo.genero})

    def verifica_dados_compra(self):
        informacoes_compra = self.__tela_compra.verifica_compra()
        for compra in self.__compras:
            if compra.usuario.email == informacoes_compra["email"]:
                if compra.usuario.senha == informacoes_compra["senha"]:
                    if compra.identificador == informacoes_compra["identificador"]:
                        self.__tela_compra.retorna_informacoes_compra({"jogo": compra.jogo.nome, "usuario": compra.usuario.nome, "data": compra.data})

    def retorna_menu_principal(self):
        self.__continua_nesse_menu = False