


class Usuario:
    def __init__(self, email: str, senha: str, nome: str, idade: int):
        self.__email = email
        self.__senha = senha
        self.__nome = nome
        self.__idade = idade

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade
