class EmailInvalidoException(Exception):
    def __init__(self):
        super().__init__("Formato de email invalido ou email não existe! Um email valido segue o padrao: exemplo@gmail.com ")