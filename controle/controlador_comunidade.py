from limite.tela_comunidade import TelaComunidade
from limite.tela_comunidade_cria import TelaComunidadeCria
from limite.tela_comunidade_remove import TelaComunidadeRemove
from limite.tela_comunidade_add_usuario import TelaComunidadeAddUsuario
from limite.tela_comunidade_del_usuario import TelaComunidadeDelUsuario
from limite.tela_comunidade_verificador import TelaComunidadeVerificador
from limite.tela_comunidade_busca_nome import TelaComunidadeBuscaNome
from limite.tela_comunidade_alterar import TelaComunidadeAltera
from entidade.comunidade import Comunidade
from excecoes.usuario_invalido_exception import UsuarioInvalidoException
from excecoes.comunidade_invalida_exception import ComunidadeInvalidaException
from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.email_invalido_exception import EmailInvalidoException
import string


class ControladorComunidade:
    def __init__(self, controlador_sistema):
        self.__comunidades = []
        self.__tela_comunidade = TelaComunidade()
        self.__tela_comunidade_cria = TelaComunidadeCria()
        self.__tela_comunidade_remove = TelaComunidadeRemove()
        self.__tela_comunidade_add_usuario = TelaComunidadeAddUsuario()
        self.__tela_comunidade_del_usuario = TelaComunidadeDelUsuario()
        self.__tela_comunidade_verificador = TelaComunidadeVerificador()
        self.__tela_comunidade_busca_nome = TelaComunidadeBuscaNome()
        self.__tela_comunidade_altera = TelaComunidadeAltera()
        self.__usuarios = None
        self.__controlador_sistema = controlador_sistema
        self.__continua_nesse_menu = True

    def add_usuarios(self, usuarios):
        self.__usuarios = usuarios

    def abre_tela(self):
        lista_opcoes = {1: self.cria_comunidade, 2: self.adicionar_usuario_a_comunidade,
                        3: self.excluir_usuario_da_comunidade, 4: self.busca_comunidade_por_nome,
                        5: self.lista_comunidades,6: self.altera_comunidade,
                        7: self.remove_comunidade, 0: self.retorna_menu_principal}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_comunidade.open()]()

    def cria_comunidade(self):
        while True:
            dados_comunidade = self.__tela_comunidade_cria.open()
            if dados_comunidade[0] == 'Enviar':
                try:
                    nome_comunidade = dados_comunidade[1]['nome']
                    descricao_comunidade = dados_comunidade[1]['descricao']
                    if len(self.__comunidades) != 0:
                        if nome_comunidade in self.nome_comunidades():
                            raise ComunidadeInvalidaException
                    for digito in nome_comunidade:
                        if digito not in string.ascii_letters and digito not in [" ", "  "]:
                            raise NomeInvalidoException
                    comunidade = Comunidade(nome_comunidade, descricao_comunidade)
                    self.__comunidades.append(comunidade)
                    self.__tela_comunidade.close()
                    break
                except ComunidadeInvalidaException as e:
                    self.__tela_comunidade.show_message('Aviso', str(e))
                except NomeInvalidoException as e:
                    self.__tela_comunidade.show_message('Aviso', str(e))
            else:
                self.__tela_comunidade.show_message("Aviso", "Processo Cancelado")
                break

    def remove_comunidade(self):
        if len(self.__comunidades) == 0:
            self.__tela_comunidade.show_message("Aviso ", "Não existem comunidades cadastradas!")
        else:
            dados_comunidade = self.__tela_comunidade_remove.open()
            nome = dados_comunidade[1]['nome']
            comunidade = self.comunidade_by_nome(nome)
            if dados_comunidade[0] == 'Enviar':
                try:
                    if nome not in self.nome_comunidades():
                        raise NomeInvalidoException
                    for digito in nome:
                        if digito not in string.ascii_letters and digito not in [" ", "  "]:
                            raise NomeInvalidoException
                    self.__comunidades.remove(comunidade)
                    self.__tela_comunidade.close()
                except NomeInvalidoException:
                    self.__tela_usuario.show_message('Aviso', 'Nome invalido ou nome já utilizado!')
            else:
                self.__tela_usuario_verificador.show_message("Aviso", "Processo Cancelado")

    def adicionar_usuario_a_comunidade(self):
        if len(self.__comunidades) == 0:
            self.__tela_comunidade.show_message("Aviso!", "Nao existem comunidades disponiveis!")
        elif len(self.__usuarios) == 0:
            self.__tela_comunidade.show_message("Aviso!", "Nao existem usuarios disponiveis!")
        else:
            while True:
                dados = self.__tela_comunidade_add_usuario.open(self.nome_comunidades())
                # dados -> ('Enviar', {'email': 'b@gmail.com', 'comunidade_escolhida': 'solitario'})
                comunidade = self.comunidade_by_nome(dados[1]['nome_comunidade'])
                usuario = self.usuario_by_email(dados[1]['email'])
                email_usuario = dados[1]['email']
                if dados[0] == 'Enviar':
                    try:
                        if email_usuario not in self.emails_usuarios():
                            raise EmailInvalidoException
                        if "@" not in dados[1]['email']:
                            raise EmailInvalidoException
                        entrada = dados[1]['email'].split("@")
                        if entrada[1] != "gmail.com":
                            raise EmailInvalidoException
                        comunidade.incluir_usuario(usuario)
                        usuario.incluir_comunidade(comunidade)
                        break
                    except EmailInvalidoException as e:
                        self.__tela_comunidade.show_message('Aviso', str(e))
                else:
                    self.__tela_comunidade.show_message("Aviso", "Processo Cancelado")
                    break

    def excluir_usuario_da_comunidade(self):
        if len(self.__comunidades) == 0:
            self.__tela_comunidade.show_message("Aviso!", "Nao existem comunidades disponiveis!")
        elif len(self.__usuarios) == 0:
            self.__tela_comunidade.show_message("Aviso!", "Nao existem usuarios disponiveis!")
        else:
            email = self.__tela_comunidade_verificador.open()
            if email[0] == 'Enviar':
                try:
                    if email[1]['email'] not in self.emails_usuarios():
                        raise EmailInvalidoException
                    for usuario in self.__usuarios:
                        if usuario.email == email[1]['email']:
                            self.comunidade_remove_usuario(usuario)
                        else:
                            self.__tela_comunidade.show_message("Aviso", "Email invalido ou inexistente!")
                except EmailInvalidoException as e:
                    self.__tela_comunidade.show_message("Aviso", str(e))
            else:
                self.__tela_comunidade.show_message("Aviso!", "Processo Cancelado")

    def comunidade_remove_usuario(self, usuario):
        comunidades_nome = self.comunidades_do_usuario(usuario)
        dado = self.__tela_comunidade_del_usuario.open(comunidades_nome)
        if dado[0] == 'Enviar':
            for comunidade in usuario.comunidades:
                for i in comunidades_nome:
                    if i == comunidade.nome:
                        usuario.excluir_comunidade(comunidade)
                        comunidade.excluir_usuario(usuario)
        else:
            self.__tela_comunidade_del_usuario.show_message("Aviso", "Processo cancelado")

    def busca_comunidade_por_nome(self):
        if len(self.__comunidades) == 0:
            self.__tela_comunidade.show_message("Aviso!", "Nao existem comunidades disponiveis!")
        else:
            while True:
                dados = self.__tela_comunidade_busca_nome.open()
                if dados[0] == 'Enviar':
                    try:
                        if dados[1]['nome'] not in self.nome_comunidades():
                            raise NomeInvalidoException
                        for comunidade in self.__comunidades:
                            if comunidade.nome == dados[1]['nome']:
                                self.__tela_comunidade_busca_nome.show_message("Comunidade " + comunidade.nome.upper(),
                                                                               "Descricao: " + comunidade.descricao +
                                                                               "\nParticipantes: " + str(len(comunidade.usuarios)))
                                break
                    except NomeInvalidoException as e:
                        self.__tela_comunidade.show_message('Aviso', str(e))
                        break
                else:
                    self.__tela_comunidade.show_message('Aviso', 'Processo cancelado')
                    break
                break

    def lista_comunidades(self):
        if len(self.__comunidades) == 0:
            self.__tela_comunidade.show_message("Aviso!", "Nao existem comunidades disponiveis!")
        else:
            lista_comunidades = list()
            for comunidade in self.__comunidades:
                lista_comunidades.append("\nNome da comunidade: " + comunidade.nome +
                                         "\nNumero de participantes: " + str(len(comunidade.usuarios)))
            self.__tela_comunidade.show_message("Listagem de comunidades", "\n".join(lista_comunidades))

    def altera_comunidade(self):
        if len(self.__comunidades) == 0:
            self.__tela_comunidade.show_message("Aviso!", "Nao existem comunidades cadastradas!")
        else:
            comunidade = self.__tela_comunidade_altera.open(self.nome_comunidades(), 'tela_1')
            if comunidade[0] == 'Enviar':
                dados = self.__tela_comunidade_altera.open(self.nome_comunidades(), 'tela_2')
                novo_nome = dados[1]['nome']
                nova_descricao = dados[1]['descricao']
                if dados[0] == 'Enviar':
                    try:
                        for digito in novo_nome:
                            if digito not in string.ascii_letters and digito not in [" ", "  "] and digito not in string.digits:
                                raise NomeInvalidoException
                        for i in nova_descricao:
                            if i not in string.ascii_letters and i not in [" ", "  "] and i not in string.digits:
                                raise NomeInvalidoException
                        obj_comunidade = self.comunidade_by_nome(comunidade[1]['comunidade'][0])
                        obj_comunidade.nome = novo_nome
                        obj_comunidade.descricao = nova_descricao
                    except NomeInvalidoException as e:
                        self.__tela_comunidade.show_message("Aviso", str(e))
                else:
                    self.__tela_comunidade.show_message("Aviso", "Processo cancelado")
            else:
                self.__tela_comunidade.show_message("Aviso", "Processo cancelado")

    def retorna_menu_principal(self):
        self.__continua_nesse_menu = False

    @property
    def comunidades(self):
        return self.__comunidades

    def comunidade_by_nome(self, nome):
        for comunidade in self.__comunidades:
            if comunidade.nome == nome:
                return comunidade

    def usuario_by_email(self, email):
        for usuario in self.__usuarios:
            if usuario.email == email:
                return usuario

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

    def comunidades_do_usuario(self, user):
        comunidades = []
        for usuario in self.__usuarios:
            if usuario == user:
                for comunidade in usuario.comunidades:
                    comunidades.append(comunidade.nome)
        return comunidades
