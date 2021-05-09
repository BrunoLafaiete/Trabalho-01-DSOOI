class ValidadeInvalidaException(Exception):
    def __init__(self):
        super().__init__("Data de validade invalida! Digite a data correta!")