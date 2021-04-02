class NomeInvalidoException(Exception):
    def __init__(self):
        super().__init__("Nome invalido! Insira um nome valido:")
