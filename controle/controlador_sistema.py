from limite.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        