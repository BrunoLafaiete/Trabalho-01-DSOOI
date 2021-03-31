from entidade.loja import Loja
from limite.tela_loja import TelaLoja


class ControladorLoja:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaLoja()
        self.__loja = None
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {1: self.listar_jogos, 2: self.buscar_por_genero, 3: self.buscar_por_desenvolvedora,
                        4: self.buscar_por_faixa_etaria, 5: self.buscar_por_preco, 0: self.voltar}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela.tela_opcoes()]()

    def incluir_loja(self, jogos):
        self.__loja = Loja(jogos)

    def listar_jogos(self):
        for jogo in self.__loja.jogos:
            self.__tela.mostrar_jogo({"nome": jogo.nome, "desenvolvedora": jogo.desenvolvedora,
                                      "genero": jogo.genero, "faixa etaria": jogo.faixa_etaria,
                                      "preco": jogo.preco})

    def buscar_por_genero(self):
        genero = self.__tela.conseguir_genero(self.__loja.generos)
        for jogo in self.__loja.jogos:
            if genero == jogo.genero:
                self.__tela.mostrar_jogo({"nome": jogo.nome, "desenvolvedora": jogo.desenvolvedora,
                                          "genero": jogo.genero, "faixa etaria": jogo.faixa_etaria,
                                          "preco": jogo.preco})

    def buscar_por_desenvolvedora(self):
        desenvolvedora = self.__tela.conseguir_desenvolvedora(self.__loja.desenvolvedoras)
        for jogo in self.__loja.jogos:
            if jogo.desenvolvedora.nome == desenvolvedora:
                self.__tela.mostrar_jogo({"nome": jogo.nome, "desenvolvedora": jogo.desenvolvedora,
                                          "genero": jogo.genero, "faixa etaria": jogo.faixa_etaria,
                                          "preco": jogo.preco})

    def buscar_por_faixa_etaria(self):
        idades = self.__tela.conseguir_idade()
        for jogo in self.__loja.jogos:
            if min(idades) <= jogo.faixa_etaria <= max(idades):
                self.__tela.mostrar_jogo({"nome": jogo.nome, "desenvolvedora": jogo.desenvolvedora,
                                          "genero": jogo.genero, "faixa etaria": jogo.faixa_etaria,
                                          "preco": jogo.preco})

    def buscar_por_preco(self):
        precos = self.__tela.conseguir_preco()
        for jogo in self.__loja.jogos:
            if min(precos) <= jogo.preco <= max(precos):
                self.__tela.mostrar_jogo({"nome": jogo.nome, "desenvolvedora": jogo.desenvolvedora,
                                          "genero": jogo.genero, "faixa etaria": jogo.faixa_etaria,
                                          "preco": jogo.preco})

    def voltar(self):
        self.__continua_nesse_menu = False
