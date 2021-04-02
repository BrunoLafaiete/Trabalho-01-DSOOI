class DesenvolvedoraInvalidaException(Exception):
    def __init__(self):
        super().__init__("Desenvolvedora invalida! Digite uma desenvolvedora correta: ")
