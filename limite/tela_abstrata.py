from abc import ABC, abstractmethod


class TelaAbstrata(ABC):

    @abstractmethod
    def tela_opcoes(self):
        pass
   
    def le_num_int(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor invalido: Digite um valor numerico inteiro valido")
                if inteiros_validos:
                    print("Valores validos: ", inteiros_validos)

    def le_lista(self, lista: [] = None):
        mensagem = ""
        for item in lista:
            mensagem += str(item) + ", "

        return mensagem[:-2]
