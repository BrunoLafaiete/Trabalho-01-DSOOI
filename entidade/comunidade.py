class Comunidade:
    def __init__(self, nome: str, descricao: str):
        self.__nome = nome
        self.__descricao = descricao
        self.__jogo = None
        self.__usuarios = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def jogo(self):
        return self.__jogo

    @jogo.setter
    def jogo(self, jogo):
        self.__jogo.append(jogo)

    @property
    def usuarios(self):
        return self.__usuarios

    @usuarios.setter
    def usuarios(self, usuario):
        self.__usuarios.append(usuario)
