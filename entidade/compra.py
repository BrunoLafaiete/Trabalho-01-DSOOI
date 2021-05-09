from datetime import date
from entidade.jogo import Jogo
from entidade.usuario import Usuario


class Compra:

    def __init__(self, jogo: Jogo, usuario: Usuario):
        self.__jogo = jogo
        self.__jogo.incluir_compra(self)
        self.__usuario = usuario
        self.__usuario.incluir_compra(self)
        self.__usuario.jogos.append(jogo)
        self.__data = date.today()
        self.__id = id(self)

    @property
    def data(self):
        return self.__data

    @property
    def jogo(self):
        return self.__jogo

    @property
    def usuario(self):
        return self.__usuario

    @property
    def id(self):
        return self.__id