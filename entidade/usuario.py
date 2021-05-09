from entidade.cartao_de_credito import CartaoDeCredito
from entidade.pessoa import Pessoa


class Usuario(Pessoa):

    def __init__(self, email: str, senha: str, nome: str, idade: int):
        super().__init__(email, senha, nome, idade)
        self.__email = email
        self.__senha = senha
        self.__nome = nome
        self.__idade = idade
        self.__saldo = 0
        self.__comunidades = []
        self.__jogos = []
        self.__compras = []
        self.__cartao = None
        self.__id = id(self)

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

    def incluir_compra(self, compra):
        self.__compras.append(compra)

    def remover_compra(self, compra):
        self.__compras.remove(compra)

    @property
    def comunidades(self):
        return self.__comunidades

    def incluir_comunidade(self, comunidade):
        self.__comunidades.append(comunidade)

    def excluir_comunidade(self, comunidade):
        self.__comunidades.remove(comunidade)

    @property
    def jogos(self):
        return self.__jogos

    def incluir_jogo(self, jogo):
        self.__jogos.append(jogo)

    def remover_jogo(self, jogo):
        self.__jogos.remove(jogo)

    @property
    def cartao(self):
        return self.__cartao

    @cartao.setter
    def cartao(self, cartao: CartaoDeCredito):
        self.__cartao = cartao

    def add_cartao(self, nome, instituicao, numero, validade, codigo_seguranca):
        self.__cartao = CartaoDeCredito(nome, instituicao, numero, validade, codigo_seguranca)

    def altera_cartao(self, nome, instituicao, numero, validade, codigo_seguranca):
        self.__cartao.nome_portador = nome
        self.__cartao.instituicao = instituicao
        self.__cartao.numero = numero
        self.__cartao.validade = validade
        self.__cartao.codigo_seguranca = codigo_seguranca

    def remover_cartao(self):
        self.__cartao = None

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome
