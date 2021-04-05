from datetime import date


class CartaoDeCredito:

    def __init__(self, nome_portador, instituicao, numero, validade: date, codigo_seguranca):
        self.__nome_portador = nome_portador
        self.__instituicao = instituicao
        self.__numero = numero
        self.__validade = validade
        self.__codigo_seguranca = codigo_seguranca

    @property
    def nome_portador(self):
        return self.__nome_portador

    @nome_portador.setter
    def nome_portador(self, nome_portador):
        self.__nome_portador = nome_portador

    @property
    def instituicao(self):
        return self.__instituicao

    @instituicao.setter
    def instituicao(self, instituicao):
        self.__instituicao = instituicao

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def validade(self):
        return self.__validade

    @validade.setter
    def validade(self, validade):
        self.__validade = validade

    @property
    def codigo_seguranca(self):
        return self.__codigo_seguranca

    @codigo_seguranca.setter
    def codigo_seguranca(self, codigo_seguranca):
        self.__codigo_seguranca = codigo_seguranca
