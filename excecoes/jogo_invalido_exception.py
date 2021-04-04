class JogoInvalidoException(Exception):
    def __init__(self):
        super().__init__("Jogo invalido! Digite o nome de um jogo valido que esteja na loja ")