from limite.tela_usuario import TelaUsuario

class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        self.__tela_usuario.tela_opcoes()
