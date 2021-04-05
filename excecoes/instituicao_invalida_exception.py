class InstituicaoInvalidaException(Exception):
    def __init__(self):
        super().__init__("Instituicao invalida")