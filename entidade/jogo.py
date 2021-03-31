from entidade.compra import Compra


class Jogo:

    def __init__(self, nome: str, desenvolvedora, genero: str,
                 faixa_etaria: int, preco: float):
        self.__nome = nome
        self.__desenvolvedora = desenvolvedora
        self.__genero = genero
        self.__faixa_etaria = faixa_etaria
        self.__preco = preco
        self.__compras = []


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def desenvolvedora(self):
        return self.__desenvolvedora

    @desenvolvedora.setter
    def desenvolvedora(self, desenvolvedora):
        self.__desenvolvedora = desenvolvedora
        #desenvolvedora.incluir_jogo(self)

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        self.__genero = genero

    @property
    def faixa_etaria(self):
        return self.__faixa_etaria

    @faixa_etaria.setter
    def faixa_etaria(self, faixa_etaria: int):
        self.__faixa_etaria = faixa_etaria

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco: float):
        self.__preco = preco

    def nova_compra(self, compra: Compra):
        self.__compras.append(compra)

    @property
    def compras(self):
        return self.__compras
