from entidade.desenvolvedora import Desenvolvedora
from limite.tela_desenvolvedora import TelaDesenvolvedora


class ControladorDesenvolvedora:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__desenvolvedoras = []
        self.__tela_desenvolvedora = TelaDesenvolvedora()
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {0: self.voltar, 1: self.cadastra_desenvolvedora, 2: self.alterar_desenvolvedora,
                        3: self.get_dados_desenvolvedora, 4: self.lista_desenvolvedoras}
        self.__continua_nesse_menu = True

        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_desenvolvedora.tela_opcoes()]()

    def cadastra_desenvolvedora(self):
        desenvolvedora = Desenvolvedora(self.__tela_desenvolvedora.cadastrar_desenvolvedora(self.__desenvolvedoras))

        self.__desenvolvedoras.append(desenvolvedora)

    def alterar_desenvolvedora(self):
        desenvolvedora = self.get_desenvolvedora_by_nome()
        nome_antigo = desenvolvedora.nome
        desenvolvedora.nome = self.__tela_desenvolvedora.alterar_desenvolvedora(self.__desenvolvedoras, nome_antigo)

    def lista_desenvolvedoras(self):
        for desenvolvedora in self.__desenvolvedoras:
            self.__tela_desenvolvedora.mostrar_desenvolvedora({"nome": desenvolvedora.nome,
                                                               "jogos": desenvolvedora.jogos})

    def voltar(self):
        self.__continua_nesse_menu = False

    def get_dados_desenvolvedora(self):
        desenvolvedora = self.get_desenvolvedora_by_nome()
        self.__tela_desenvolvedora.mostrar_desenvolvedora({"nome": desenvolvedora.nome,
                                                           "jogos": desenvolvedora.jogos})

    def get_desenvolvedora_by_nome(self):
        nome = self.__tela_desenvolvedora.escrever_nome()
        for desenvolvedora in self.__desenvolvedoras:
            if desenvolvedora.nome == nome:
                return desenvolvedora

    @property
    def desenvolvedoras(self):
        return self.__desenvolvedoras
