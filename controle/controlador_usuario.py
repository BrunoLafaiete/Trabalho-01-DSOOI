from limite.tela_usuario import TelaUsuario
from entidade.usuario import Usuario

class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_usuario, 2: self.verifica_usuario_existente, 3: self.informar_dados_usuario, 4: self.lista_usuarios,
                        5: self.credita, 0: self.retorna_menu_principal}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()

    def cadastra_usuario(self):
        dados_do_usuario = self.__tela_usuario.cadastrar_usuario()
        usuario = Usuario(dados_do_usuario["email"], dados_do_usuario["senha"], dados_do_usuario["nome"],
                          dados_do_usuario["idade"])
        self.__usuarios.append(usuario)

    def lista_usuarios(self):
        for usuario in self.__usuarios:
            self.__tela_usuario.listar_usuario({"email": usuario.email, "nome": usuario.nome, "idade": usuario.idade})

    def informar_dados_usuario(self):
        email_do_usuario = self.__tela_usuario.buscar_pelo_email()
        for usuario in self.__usuarios:
            if usuario.email == email_do_usuario:
                self.__tela_usuario.devolve_dados_usuario({"email": usuario.email, "creditos": usuario.saldo,
                                                           "nome": usuario.nome, "idade": usuario.idade})

    def credita(self):
        dados_favorecido = self.__tela_usuario.tela_credita()
        for usuario in self.__usuarios:
            if usuario.email == dados_favorecido["email"]:
                usuario.saldo += dados_favorecido["valor"]

    def verifica_usuario_existente(self):
        for usuario in self.__usuarios:
            if self.__tela_usuario.verificar_email() == usuario.email:
                if self.__tela_usuario.verificar_senha() == usuario.senha:
                   dados_usuario = self.__tela_usuario.alterar_usuario()
                   usuario.email = dados_usuario["email"]
                   usuario.senha = dados_usuario["senha"]
                   usuario.nome = dados_usuario["nome"]
                   usuario.idade = dados_usuario["idade"]

    def retorna_menu_principal(self):
        self.__continua_nesse_menu = False

