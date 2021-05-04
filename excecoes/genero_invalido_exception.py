class GeneroInvalidoException(Exception):
    def __init__(self):
        super().__init__("Genro invalido! Digite um genero que contenha pelo menos um caractere ou número")
