from entidade.jogo import Jogo
from controle.controlador_sistema import ControladorSistema
from limite.tela_jogo import TelaJogo


class ControladorJogos:

    def __init__(self, controlador: ControladorSistema):
        self.__controlador_sistema = controlador
        self.__tela_jogo = TelaJogo()
        self.__jogos = []

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_jogo, 4: self.lista_jogos}
        continua_nesse_menu = True

        while continua_nesse_menu:
            lista_opcoes[self.__tela_jogo.tela_opcoes()]()

    def cadastra_jogo(self):
        dados_jogo = self.__tela_jogo.cadastrar_jogo()
        jogo = Jogo(dados_jogo["nome"], dados_jogo["desenvolvedora"], dados_jogo["genero"],
                    dados_jogo["faixa etaria"], dados_jogo["preco"])

        self.__jogos.append(jogo)

    def lista_jogos(self):
        for jogo in self.__jogos:
            self.__tela_jogo.mostrar_jogo({"nome": jogo.nome, "desenvolvedora": jogo.desenvolvedora,
                                           "genero": jogo.genero, "faixa etaria": jogo.faixa_etaria,
                                           "preco": jogo.preco})
