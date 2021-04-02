class UsuarioInvalidoException(Exception):
    def __init__(self):
        super().__init__("O email ou senha esta errado!")
