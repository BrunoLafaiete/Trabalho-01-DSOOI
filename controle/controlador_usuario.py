from limite.tela_usuario import TelaUsuario
from entidade.usuario import Usuario

class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_usuario, 4: self.lista_usuarios}
        continua_nesse_menu = True
        while continua_nesse_menu:

            lista_opcoes[self.__tela_usuario.tela_opcoes()]()


    def cadastra_usuario(self):
        dados_do_usuario = self.__tela_usuario.cadastrar_usuario()
        usuario = Usuario(dados_do_usuario["email"], dados_do_usuario["senha"], dados_do_usuario["nome"],
                          dados_do_usuario["idade"])
        self.__usuarios.append(usuario)

    def lista_usuarios(self):
        for usuario in self.__usuarios:
            self.__tela_usuario.mostrar_usuario({"email": usuario.email, "nome": usuario.nome, "idade": usuario.idade})