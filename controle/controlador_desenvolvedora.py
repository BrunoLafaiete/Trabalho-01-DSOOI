from entidade.desenvolvedora import Desenvolvedora
from limite.tela_desenvolvedora import TelaDesenvolvedora

class ControladorDesenvolvedoras:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__desenvolvedoras = []
        self.__tela_desenvolvedora = TelaDesenvolvedora()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_desenvolvedora, 4: self.lista_desenvolvedoras}
        continua_nesse_menu = True

        while continua_nesse_menu:
            lista_opcoes[self.__tela_desenvolvedora.tela_opcoes()]()

    def cadastra_desenvolvedora(self):
        desenvolvedora = Desenvolvedora(self.__tela_desenvolvedora.cadastrar_desenvolvedora())

        self.__desenvolvedoras.append(desenvolvedora)

    def lista_desenvolvedoras(self):
        for desenvolvedora in self.__desenvolvedoras:
            self.__tela_desenvolvedora.mostrar_desenvolvedora({"nome": desenvolvedora.nome, "jogos": desenvolvedora.jogos})
