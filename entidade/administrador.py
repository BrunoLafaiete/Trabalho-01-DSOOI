from entidade.pessoa import Pessoa

class Administrador(Pessoa):
    def __init__(self, email: str, senha: str, nome: str, idade: int):
        super().__init__(email, senha, nome, idade)
        self.__email = email
        self.__senha = senha
        self.__nome = nome
        self.__idade = idade
        self.__comunidades_administradas = []

    @property
    def comunidades_administradas(self):
        return self.__comunidades_administradas
