from datetime import date


class Compra:
    def __init__(self, jogo, usuario):
        self.__jogo = jogo
        self.__usuario = usuario
        self.__data = date.today()

    @property
    def data(self):
        return data

    @property
    def jogo(self):
        return jogo

    @property
    def usuario(self):
        return usuario