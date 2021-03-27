from limite.tela_sistema import TelaSistema
from controle.controlador_usuario import ControladorUsuario
from controle.controlador_jogo import ControladorJogos
'''from controle.controlador_loja import ControladorLoja
from controle.controlador_compra import ControladorCompra
from controle.controlador_comunidade import ControladorComunidade'''''
from controle.controlador_desenvolvedora import ControladorDesenvolvedoras


class ControladorSistema:
    def __init__(self):
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_jogo = ControladorJogos(self)
        '''self.__controlador_loja = ControladorLoja(self)
        self.__controlador_compra = ControladorCompra(self)
        self.__controlador_comunidade = ControladorComunidade(self)'''
        self.__controlador_desenvolvedora = ControladorDesenvolvedoras(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.jogo, 2: self.loja, 3: self.compra, 4: self.usuario,
                        5: self.comunidade, 6: self.desenvolvedora ,7: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_inicial()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def usuario(self):
        pass
        self.__controlador_usuario.abre_tela()

    def jogo(self):
        self.__controlador_jogo.abre_tela()

    def loja(self):
        pass

    def compra(self):
        pass

    def comunidade(self):
        pass

    def desenvolvedora(self):
        self.__controlador_desenvolvedora.abre_tela()

    def encerra_sistema(self):
        exit(0)
