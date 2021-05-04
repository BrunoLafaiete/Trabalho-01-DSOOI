class IdadeInvalidaException(Exception):
    def __init__(self):
        super().__init__("Idade invalida! Digite uma idade valida (entre 1 e 130)! ")