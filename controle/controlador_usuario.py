from limite.tela_usuario import TelaUsuario
from limite.tela_usuario_cadastro import TelaUsuarioCadastro
from limite.tela_usuario_verificador import TelaUsuarioVerificador
from entidade.usuario import Usuario
from controle.controlador_cartao_de_credito import ControladorCartaodeCredito
from excecoes.email_invalido_exception import EmailInvalidoException
from excecoes.senha_invalida_exception import SenhaInvalidaException
from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.idade_invalida_exception import IdadeInvalidaException 
import string


class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__tela_usuario_cadastro = TelaUsuarioCadastro()
        self.__tela_usuario_verificador = TelaUsuarioVerificador()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_cartao_de_credito = ControladorCartaodeCredito()
        self.__continua_nesse_menu = True
        self.__compras = None

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_usuario, 2: self.alterar_dados_usuario,
                        3: self.informar_dados_usuario, 4: self.lista_usuarios,
                        5: self.credita, 6: self.cartao_de_credito, 0: self.retorna_menu_principal}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_usuario.open()]()

    def cadastra_usuario(self):
        while True:
            dados_usuario = self.__tela_usuario_cadastro.open()
            if dados_usuario[0] == 'Enviar':
                try:
                    for user in self.usuarios:
                        if user.email == dados_usuario[1]['email']:
                            raise EmailInvalidoException
                    if "@" not in dados_usuario[1]['email']:
                        raise EmailInvalidoException
                    else:
                        entrada = dados_usuario[1]['email'].split("@")
                        if entrada[1] != "gmail.com":
                            raise EmailInvalidoException
                    for digito in dados_usuario[1]['senha']:
                        if digito not in string.printable:
                            raise SenhaInvalidaException
                    for letra in dados_usuario[1]['nome']:
                        if letra not in string.ascii_letters and letra not in [" ", "  "]:
                            raise NomeInvalidoException
                    idade = int(dados_usuario[1]['idade'])
                    if 0 > idade or 130 < idade:
                        raise IdadeInvalidaException
                    break
                except EmailInvalidoException as e:
                    self.__tela_usuario.show_message('Erro!', str(e))
                except SenhaInvalidaException as e:
                    self.__tela_usuario.show_message('Erro!', str(e))
                except NomeInvalidoException as e:
                    self.__tela_usuario.show_message('Erro!', str(e))
                except IdadeInvalidaException as e:
                    self.__tela_usuario.show_message('Erro!', str(e))
            else:
                self.__tela_usuario.show_message("Aviso", "Processo Cancelado")
                break
        usuario = Usuario(dados_usuario[1]['email'], dados_usuario[1]['senha'],
                          dados_usuario[1]['nome'], dados_usuario[1]['idade'])
        self.__usuarios.append(usuario)
        self.__tela_usuario.close()

    def alterar_dados_usuario(self):
        if len(self.__usuarios) == 0:
            self.__tela_usuario.show_message("Aviso!", "Não existem usuarios "
                                                       "cadastrados! Por favor cadastre pelo "
                                                       "menos um antes de alterar dados ")
        else:
            usuario = self.get_usuario_by_email()
            if usuario is not None:
                email_antigo = usuario.email
                while True:
                    try:
                        dados_usuario = self.__tela_usuario_cadastro.open()
                        if dados_usuario is not None:
                            if dados_usuario[1]['email'] in self.lista_emails_usuarios and dados_usuario[1]['email'] != email_antigo:
                                raise EmailInvalidoException
                            if "@" not in dados_usuario[1]['email']:
                                raise EmailInvalidoException
                            else:
                                entrada = dados_usuario[1]['email'].split("@")
                                if entrada[1] != "gmail.com":
                                    raise EmailInvalidoException
                            for digito in dados_usuario[1]['senha']:
                                if digito not in string.printable:
                                    raise SenhaInvalidaException
                            for letra in dados_usuario[1]['nome']:
                                if letra not in string.ascii_letters and letra not in [" ", "  "]:
                                    raise NomeInvalidoException
                            idade = int(dados_usuario[1]['idade'])
                            if 0 > idade or 130 < idade:
                                raise IdadeInvalidaException
                            break
                        else:
                            self.__tela_usuario.show_message("Aviso", "Processo Cancelado")
                            break
                    except EmailInvalidoException as e:
                        self.__tela_usuario.show_message('Erro!', str(e))
                    except SenhaInvalidaException as e:
                        self.__tela_usuario.show_message('Erro!', str(e))
                    except NomeInvalidoException as e:
                        self.__tela_usuario.show_message('Erro!', str(e))
                    except IdadeInvalidaException as e:
                        self.__tela_usuario.show_message('Erro!', str(e))
                
                if dados_usuario is not None:
                    usuario.email = dados_usuario[1]['email']
                    usuario.senha = dados_usuario[1]['senha']
                    usuario.nome = dados_usuario[1]['nome']
                    usuario.idade = dados_usuario[1]['idade']

    def remove_usuario(self, usuario: Usuario):
        if len(self.__usuarios) == 0:
            self.__tela_usuario.show_message("Aviso!", "Nao existem usuarios cadastrados!")
        else:
            self.__usuarios.remove(usuario)

    def lista_usuarios(self):
        if len(self.usuarios) == 0:
            self.__tela_usuario.show_message("Aviso!", "Não existem jogos disponiveis! "
                                                    "Por favor insira pelo menos um")
        else:
            lista_usuarios = list()
            for usuario in self.__usuarios:
                lista_usuarios.append("\nTotal de usuários cadastrados: " + str(len(self.__usuarios))
                                      + "\nNome do usuario: " + usuario.nome + "\nEmail do usuario: "
                                      + usuario.email + "\nIdade do usuario: " + usuario.idade)
            self.__tela_usuario.show_message("Listagem de Usuarios", "\n".join(lista_usuarios))

    def get_usuario_by_email(self):
        if len(self.__usuarios) == 0:
            self.__tela_usuario.show_message("Aviso!", "Não existem usuarios cadastrados! "
                                                    "Por favor cadastre pelo menos um")
        else:
            while True:
                try:
                    email = self.__tela_usuario_verificador.open()
                    if email[0] == 'Enviar':
                        for usuario in self.__usuarios:
                            if usuario.email == email[1]['email']:
                                self.__tela_usuario_verificador.close()
                                return usuario
                        raise NomeInvalidoException
                    else:
                        self.__tela_usuario_verificador.close()
                        return None
                except NomeInvalidoException as e:
                    self.__tela_usuario_verificador.show_message('Aviso', str(e))
                    self.__tela_usuario_verificador.close()

    def informar_dados_usuario(self):
        if len(self.__usuarios) == 0:
            self.__tela_usuario.show_message("Aviso!", "Não existem usuarios cadastrados! "
                                                    "Por favor cadastre pelo menos um")
        else:
            email = self.__tela_usuario_verificador.open()
            if email[0] == 'Enviar':
                for usuario in self.__usuarios:
                    if usuario.email == email[1]['email']:
                        self.__tela_usuario.show_message(usuario.nome.upper(), "Nome do Usuario: " + usuario.nome
                                                                               + "\nEmail do usuario: " + usuario.email +
                                                                               "\nIdade do usuario: " + usuario.idade)
            else:
                self.__tela_usuario_verificador.show_message("Aviso", "Processo Cancelado")

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

    def cartao_de_credito(self):
        if len(self.__usuarios) == 0:
            self.__tela_usuario.show_message("Aviso!", "Nao existem usuarios cadastrados!")
        else:
            usuario = self.get_usuario_by_nome()
            if usuario.senha == self.__tela_usuario.verificar_senha():
                self.__controlador_cartao_de_credito.definir_usuario(usuario)
                self.__controlador_cartao_de_credito.abre_tela()
            else:
                self.__tela_usuario.show_message("Aviso!", "Senha invalida!")

    def retorna_menu_principal(self):
        self.__continua_nesse_menu = False

    @property
    def usuarios(self):
        return self.__usuarios

    @property
    def lista_emails_usuarios(self):
        lista_emails = []
        for usuario in self.usuarios:
            lista_emails.append(usuario.email)
        return lista_emails

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
