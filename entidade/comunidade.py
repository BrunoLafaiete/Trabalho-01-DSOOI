from entidade.usuario import Usuario

class Comunidade:
    def __init__(self, nome: str, descricao: str):
        self.__nome = nome
        self.__descricao = descricao
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
    def usuarios(self):
        return self.__usuarios

    def incluir_usuario(self, usuario: Usuario):
        self.__usuarios.append(usuario)

    def excluir_usuario(self, usuario: Usuario):
        self.__usuarios.remove(usuario)