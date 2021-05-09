from entidade.jogo import Jogo


class Desenvolvedora:

    def __init__(self, nome):
        self.__nome = nome
        self.__jogos = []
        self.__id = id(self)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def jogos(self):
        return self.__jogos

    def incluir_jogo(self, jogo: Jogo):
        self.__jogos.append(jogo)

    def excluir_jogo(self, jogo: Jogo):
        self.__jogos.remove(jogo)

    @property
    def id(self):
        return self.__id