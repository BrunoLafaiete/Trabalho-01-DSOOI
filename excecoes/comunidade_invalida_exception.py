class ComunidadeInvalidaException(Exception):
    def __init__(self):
        super().__init__("Comunidade invalida! Digite o nome de uma comunidade ativa ")