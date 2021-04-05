from limite.tela_comunidade import TelaComunidade
from entidade.comunidade import Comunidade
from excecoes.usuario_invalido_exception import UsuarioInvalidoException


class ControladorComunidade:
    def __init__(self, controlador_sistema):
        self.__comunidades = []
        self.__tela_comunidade = TelaComunidade()
        self.__usuarios = None
        self.__controlador_sistema = controlador_sistema
        self.__continua_nesse_menu = True

    def add_usuarios(self, usuarios):
        self.__usuarios = usuarios

    def abre_tela(self):
        lista_opcoes = {1: self.cria_comunidade, 2: self.adicionar_usuario_a_comunidade,
                        3: self.excluir_usuario_a_comunidade, 4: self.busca_comunidade_por_nome,
                        5: self.lista_comunidades,6: self.altera_comunidade, 0: self.retorna_menu_principal}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_comunidade.tela_opcoes()]()

    def cria_comunidade(self):
        dados_comunidade = self.__tela_comunidade.nova_comunidade(self.__comunidades)
        comunidade = Comunidade(dados_comunidade["nome"], dados_comunidade["descricao"])
        self.__comunidades.append(comunidade)

    def remove_comunidade(self):
        if len(self.__comunidades) == 0:
            self.__tela_comunidade.mostra_mensagem_erro("Não existem comunidades disponiveis!")
        else:
            comunidade = self.get_comunidade_by_nome()
            for usuario in comunidade.usuarios:
                usuario.excluir_comunidade(comunidade)
            self.__comunidades.remove(comunidade)

    def get_comunidade_by_nome(self):
        while True:
            try:
                nome = self.__tela_comunidade.pega_nome()
                for comunidade in self.__comunidades:
                    if comunidade.nome == nome:
                        return comunidade
                raise NomeInvalidoException
            except NomeInvalidoException:
                self.__tela_comunidade.mostra_mensagem_erro("Insira um nome de comunidade valido")

    def adicionar_usuario_a_comunidade(self):
        if len(self.__comunidades) == 0:
            self.__tela_comunidade.mostra_mensagem_erro("Nao existem comunidades disponiveis!")
        elif len(self.__usuarios) == 0:
            self.__tela_comunidade.mostra_mensagem_erro("Nao existem usuarios disponiveis!")
        else:
            self.__tela_comunidade.add_usuario()
            usuario = self.get_usuario()
            comunidade = self.__tela_comunidade.busca_comunidade(self.__comunidades, self.nome_comunidades())
            if usuario not in comunidade.usuarios:
                comunidade.incluir_usuario(usuario)
                usuario.incluir_comunidade(comunidade)
            else:
                self.__tela_comunidade.mostra_mensagem_erro("O usuario ja esta nesta comunidade")

    def excluir_usuario_a_comunidade(self):
        if len(self.__comunidades) == 0:
            self.__tela_comunidade.mostra_mensagem_erro("Nao existem comunidades disponiveis!")
        elif len(self.__usuarios) == 0:
            self.__tela_comunidade.mostra_mensagem_erro("Nao existem usuarios disponiveis!")
        else:
            self.__tela_comunidade.remove_usuario()
            usuario = self.get_usuario()
            comunidade = self.__tela_comunidade.busca_comunidade(self.__comunidades, self.nome_comunidades())
            if usuario in comunidade.usuarios:
                comunidade.excluir_usuario(usuario)
                usuario.excluir_comunidade(comunidade)
            else:
                self.__tela_comunidade.mostra_mensagem_erro("O usuario nao esta nesta comunidade")

    def busca_comunidade_por_nome(self):
        if len(self.__comunidades) == 0:
            self.__tela_comunidade.mostra_mensagem_erro("Nao existem comunidades disponiveis!")
        else:
            comunidade = self.__tela_comunidade.busca_comunidade(self.__comunidades, self.nome_comunidades())
            self.__tela_comunidade.retorna_comunidade({"nome": comunidade.nome,
                                                       "descricao": comunidade.descricao,
                                                       "numero_participantes": len(comunidade.usuarios)})

    def lista_comunidades(self):
        if len(self.__comunidades) == 0:
            self.__tela_comunidade.mostra_mensagem_erro("Nao existem comunidades disponiveis!")
        else:
            self.__tela_comunidade.print_comunidades_ativas()
            for comunidade in self.__comunidades:
                self.__tela_comunidade.mostra_comunidades({"nome": comunidade.nome, "descricao": comunidade.descricao,
                                                           "numero_usuarios": len(comunidade.usuarios)})

    def altera_comunidade(self):
        if len(self.__comunidades) == 0:
            self.__tela_comunidade.mostra_mensagem_erro("Nao existem comunidades disponiveis!")
        else:
            comunidade = self.__tela_comunidade.busca_comunidade(self.__comunidades, self.nome_comunidades())
            dados_comunidade = self.__tela_comunidade.altera_comunidade(self.__comunidades, comunidade.nome)
            comunidade.nome = dados_comunidade["nome"]
            comunidade.descricao = dados_comunidade["descricao"]

    def existe_comunidade(self, name):
        for comunidade in self.__comunidades:
            if comunidade.nome == name:
                return True


    def retorna_menu_principal(self):
        self.__continua_nesse_menu = False

    @property
    def comunidades(self):
        return self.__comunidades

    def get_comunidade_by_nome(self):
        self.__tela_comunidade.busca_comunidade(self.__comunidades, self.nome_comunidades())

    def get_usuario(self):
        while True:
            dados_usuario = self.__tela_comunidade.encontrar_usuario()
            usuario_email = dados_usuario["email"]
            usuario_senha = dados_usuario["senha"]
            try:
                for usuario in self.__usuarios:
                    if usuario.senha == usuario_senha and usuario.email == usuario_email:
                        return usuario
                    raise UsuarioInvalidoException
            except UsuarioInvalidoException:
                self.__tela_comunidade.mostra_mensagem_erro("Usuario ou Senha invalidos!")


    def emails_usuarios(self):
        lista_emails = []
        for usuario in self.__usuarios:
            lista_emails.append(usuario.email)
        return lista_emails

    def nome_comunidades(self):
        lista_nomes = []
        for comunidade in self.__comunidades:
            lista_nomes.append(comunidade.nome)
        return lista_nomes
