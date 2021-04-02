from entidade.pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, email: str, senha: str, nome: str, idade: int):
        super().__init__(email, senha, nome, idade)
        self.__email = email
        self.__senha = senha
        self.__nome = nome
        self.__idade = idade
        self.__saldo = 0
        self.__jogos = []
        self.__compras = []

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo: float):
        if isinstance(saldo, float):
            self.__saldo = saldo

    def credite(self, valor):
        if isinstance(valor, float):
            self.__saldo += valor

    def debite(self, valor):
        if isinstance(valor, float):
            self.__saldo -= valor

    @property
    def compras(self):
        return self.__compras

    @property
    def jogos(self):
        return self.__jogos

    def incluir_compra(self, compra):
        self.__compras.append(compra)

    def remover_compra(self, compra):
        self.__compras.remove(compra)
