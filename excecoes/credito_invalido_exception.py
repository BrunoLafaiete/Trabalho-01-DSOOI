class CreditoInvalidoException(Exception):
    def __init__(self):
        super().__init__("Valor invalido! Digite um valor entre 1 e 500 ")