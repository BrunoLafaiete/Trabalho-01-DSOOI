class NumeroCartaoInvalidoException(Exception):
    def __init__(self):
        super().__init__("Numero de cartao invalido! Insira um numero com "
                         "14 ou 15 diditos numericos!")