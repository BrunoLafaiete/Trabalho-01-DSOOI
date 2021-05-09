from abc import ABC, abstractmethod


class Pessoa(ABC):

    @abstractmethod
    def __init__(self, email: str, senha: str, nome: str, idade: int):
        self.__email = email
        self.__senha = senha
        self.__nome = nome
        self.__idade = idade
        self.__saldo = 0
        self.__compras = []

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        if isinstance(email, str):
            self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        if isinstance(senha, str):
            self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        if isinstance(idade, int):
            self.__idade = idade