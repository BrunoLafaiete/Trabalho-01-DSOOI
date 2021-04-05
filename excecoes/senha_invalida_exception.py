class SenhaInvalidaException(Exception):
    def __init__(self):
        super().__init__("Senha invalida! ")