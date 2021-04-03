from limite.tela_sistema import TelaSistema
from controle.controlador_usuario import ControladorUsuario
from controle.controlador_comunidade import ControladorComunidade
from controle.controlador_compra import ControladorCompra
from controle.controlador_jogo import ControladorJogo
from controle.controlador_loja import ControladorLoja
from controle.controlador_desenvolvedora import ControladorDesenvolvedora


class ControladorSistema:
    def __init__(self):
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_comunidade = ControladorComunidade(self)
        self.__controlador_compra = ControladorCompra(self)
        self.__controlador_loja = ControladorLoja(self)
        self.__controlador_desenvolvedora = ControladorDesenvolvedora(self)
        self.__controlador_jogo = ControladorJogo(self)
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
        self.__controlador_usuario.abre_tela()

    def jogo(self):
        self.__controlador_jogo.gerar_desenvolvedoras(self.__controlador_desenvolvedora.desenvolvedoras)
        self.__controlador_jogo.abre_tela()

    @property
    def jogos_disponiveis(self):
        return self.__controlador_jogo.nomes_jogo

    def loja(self):
        if len(self.__controlador_jogo.jogos) == 0:
            self.__tela_sistema.ler_mensagem_erro("Nao existem jogos para gerar a loja! "
                                                  "Por favor insira pelo menos um jogo")
        else:
            self.__controlador_loja.incluir_loja(self.__controlador_jogo.jogos)
            self.__controlador_loja.abre_tela()

    def compra(self):
        if len(self.__controlador_jogo.jogos) == 0 or len(self.__controlador_usuario.usuarios) == 0:
            self.__tela_sistema.ler_mensagem_erro("Nao existem jogos ou usuarios suficientes para gerar as compras! "
                                                  "Por favor insira pelo menos um de cada")
        else:
            self.__controlador_compra.incluir_usuarios_e_jogos(self.__controlador_jogo.jogos,
                                                               self.__controlador_usuario.usuarios)
            self.__controlador_compra.abre_tela()

    def comunidade(self):
        self.__controlador_comunidade.abre_tela()

    def desenvolvedora(self):
        self.__controlador_desenvolvedora.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def controlador_usuario(self):
        return self.__controlador_usuario

    def controlador_jogo(self):
        return self.__controlador_jogo

    def controlador_desenvolvedora(self):
        return self.__controlador_desenvolvedora

    def controlador_comunidade(self):
        return self.__controlador_comunidade

    def controlador_compra(self):
        return self.__controlador_compra
    
