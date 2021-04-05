from limite.tela_usuario import TelaUsuario
from entidade.usuario import Usuario
from excecoes.email_invalido_exception import EmailInvalidoException


class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema
        self.__continua_nesse_menu = True
        self.__compras = None

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_usuario, 2: self.verifica_usuario_existente, 3: self.informar_dados_usuario,
                        4: self.lista_usuarios, 5: self.credita, 0: self.retorna_menu_principal}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()

    def cadastra_usuario(self):
        dados_do_usuario = self.__tela_usuario.cadastrar_usuario(self.__usuarios)
        usuario = Usuario(dados_do_usuario["email"], dados_do_usuario["senha"], dados_do_usuario["nome"],
                          dados_do_usuario["idade"])
        self.__usuarios.append(usuario)

    def remove_usuario(self):
        if len(self.__usuarios) == 0:
            self.__tela_usuario.mostra_mensagem_erro("Nao existem usuarios cadastrados!")
        else:
            usuario = self.get_usuario_by_nome()
            for comunidade in usuario.comunidades:
                comunidade.excluir_usuario(usuario)
            for compra in usuario.compras:
                compra.jogo.remover_compra(compra)
            for compra in self.__compras:
                if compra.usuario == usuario:
                    self.__compras.remove(compra)

            self.__usuarios.remove(usuario)

    def lista_usuarios(self):
        for usuario in self.__usuarios:
            self.__tela_usuario.listar_usuario({"email": usuario.email, "nome": usuario.nome, "idade": usuario.idade})

    def get_usuario_by_nome(self):
        while True:
            try:
                email = self.__tela_usuario.verificar_email()
                for usuario in self.__usuarios:
                    if usuario.email == email:
                        return usuario
                raise EmailInvalidoException
            except EmailInvalidoException:
                self.__tela_usuario.mostra_mensagem_erro("Insira um email valido!")

    def informar_dados_usuario(self):
        email_do_usuario = self.__tela_usuario.buscar_pelo_email(self.__usuarios)
        for usuario in self.__usuarios:
            if usuario.email == email_do_usuario:
                self.__tela_usuario.devolve_dados_usuario({"email": usuario.email, "creditos": usuario.saldo,
                                                           "nome": usuario.nome, "idade": usuario.idade,
                                                           "comunidades": self.ler_comunidades(usuario),
                                                           "jogos": self.ler_jogos(usuario)})

    def credita(self):
        dados_favorecido = self.__tela_usuario.tela_credita(self.__usuarios)
        for usuario in self.__usuarios:
            if usuario.email == dados_favorecido["email"]:
                usuario.credite(dados_favorecido["valor"])

    def verifica_usuario_existente(self):
        for usuario in self.__usuarios:
            if self.__tela_usuario.verificar_email() == usuario.email:
                if self.__tela_usuario.verificar_senha() == usuario.senha:
                    dados_usuario = self.__tela_usuario.alterar_usuario(self.__usuarios, usuario.email)
                    usuario.email = dados_usuario["email"]
                    usuario.senha = dados_usuario["senha"]
                    usuario.nome = dados_usuario["nome"]
                    usuario.idade = dados_usuario["idade"]

    def retorna_menu_principal(self):
        self.__continua_nesse_menu = False

    @property
    def usuarios(self):
        return self.__usuarios

    def ler_jogos(self, usuario):
        lista_jogos = []
        for jogo in usuario.jogos:
            lista_jogos.append(jogo.nome)
        return lista_jogos

    def ler_comunidades(self, usuario):
        lista_comunidades = []
        for comunidade in usuario.comunidades:
            lista_comunidades.append(comunidade.nome)
        return lista_comunidades

    def gerar_compras(self, compras):
        self.__compras = compras
