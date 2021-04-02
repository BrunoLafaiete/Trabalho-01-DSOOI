class JahPossuiJogoException(Exception):
    def __init__(self):
        super().__init__("O Usuario jah possui esse jogo")