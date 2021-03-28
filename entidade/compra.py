from datetime import date


class Compra:
    def __init__(self, jogo: Jogo, usuario: Usuario):
        self.__jogo = jogo
        self.__usuario = usuario
        self.__data = date.today()
        identificador = 0
        self.__identificador = identificador
        identificador += 1

    @property
    def data(self):
        return data

    @property
    def jogo(self):
        return jogo

    @property
    def usuario(self):
        return usuario