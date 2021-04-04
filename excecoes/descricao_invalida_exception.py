class DescricaoInvalidaException(Exception):
    def __init__(self):
        super().__init__("Descricao invalida! Utilize somente letras sem acento e os seguintes sinais: , . ; - : ")