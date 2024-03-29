from limite.tela_usuario import TelaUsuario
from limite.tela_usuario_cadastro import TelaUsuarioCadastro
from limite.tela_usuario_verificador import TelaUsuarioVerificador
from limite.tela_usuario_credita import TelaUsuarioCredita
from limite.tela_usuario_verifica_senha import TelaUsuarioVerificaSenha
from entidade.usuario import Usuario
from controle.controlador_cartao_de_credito import ControladorCartaodeCredito
from excecoes.email_invalido_exception import EmailInvalidoException
from excecoes.senha_invalida_exception import SenhaInvalidaException
from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.idade_invalida_exception import IdadeInvalidaException
from persistencia.usuariodao import UsuarioDAO
import string


class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__usuariodao = UsuarioDAO()
        self.__tela_usuario = TelaUsuario()
        self.__tela_usuario_cadastro = TelaUsuarioCadastro()
        self.__tela_usuario_verificador = TelaUsuarioVerificador()
        self.__tela_usuario_credita = TelaUsuarioCredita()
        self.__tela_usuario_verifica_senha = TelaUsuarioVerificaSenha()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_cartao_de_credito = ControladorCartaodeCredito(self)
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {0: self.voltar, 1: self.cadastra_usuario,
                        2: self.alterar_dados_usuario, 3: self.informar_dados_usuario,
                        4: self.lista_usuarios, 5: self.credita, 6: self.cartao_de_credito}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_usuario.open()]()
            self.__tela_usuario.close()

    def cadastra_usuario(self):
        while True:
            dados_usuario = self.__tela_usuario_cadastro.open()
            if dados_usuario[0] == 'Enviar':
                try:
                    for user in self.__usuariodao.get_all():
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
                    usuario = Usuario(dados_usuario[1]['email'], dados_usuario[1]['senha'],
                                      dados_usuario[1]['nome'], int(dados_usuario[1]['idade']))
                    self.__usuariodao.add(usuario.id, usuario)
                    self.__tela_usuario_cadastro.close()
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

    def alterar_dados_usuario(self):
        if len(self.__usuariodao.get_all()) == 0:
            self.__tela_usuario.show_message("Aviso!", "Não existem usuarios "
                                                       "cadastrados! Por favor cadastre pelo "
                                                       "menos um antes de alterar dados ")
        else:
            usuario = self.get_usuario_by_email()
            if usuario is not None:
                email_antigo = usuario[0].email
                while True:
                    try:
                        dados_usuario = self.__tela_usuario_cadastro.open()
                        if dados_usuario[0] == 'Enviar':
                            if (dados_usuario[1]['email'] in self.lista_emails_usuarios() and
                                    dados_usuario[1]['email'] != email_antigo):
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
                            self.__tela_usuario_cadastro.close()
                            break
                        else:
                            self.__tela_usuario.show_message("Aviso", "Processo Cancelado")
                            self.__tela_usuario_cadastro.close()
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
                    usuario[0].email = dados_usuario[1]['email']
                    usuario[0].senha = dados_usuario[1]['senha']
                    usuario[0].nome = dados_usuario[1]['nome']
                    usuario[0].idade = int(dados_usuario[1]['idade'])
                    self.__usuariodao.add(usuario[0].id, usuario[0])
                    for compra in usuario[0].compras:
                        self.__controlador_sistema.controlador_compra.dao.add(compra.id, compra)
                        self.__controlador_sistema.controlador_jogo.dao.add(compra.jogo.id, compra.jogo)
                    for comunidade in usuario[0].comunidades:
                        self.__controlador_sistema.controlador_comunidade.dao.add(comunidade.id, comunidade)

    def lista_usuarios(self):
        if len(self.usuarios) == 0:
            self.__tela_usuario.show_message("Aviso!", "Não existem jogos disponiveis! "
                                             "Por favor insira pelo menos um")
        else:
            lista_usuarios = list()
            for usuario in self.__usuariodao.get_all():
                lista_usuarios.append("\nNome do usuario: " + usuario.nome +
                                      "\nEmail do usuario: " + usuario.email)
            self.__tela_usuario.show_message("Listagem de Usuarios" + "\nTotal de usuarios "
                                             "cadastrados: " + str(len(self.__usuariodao.get_all())),
                                             "\n".join(lista_usuarios))

    def get_usuario_by_email(self):
        if len(self.__usuariodao.get_all()) == 0:
            self.__tela_usuario.show_message("Aviso!", "Não existem usuarios cadastrados! "
                                             "Por favor cadastre pelo menos um")
        else:
            while True:
                try:
                    email = self.__tela_usuario_verificador.open()
                    if email[0] == 'Enviar':
                        for usuario in self.__usuariodao.get_all():
                            if usuario.email == email[1]['email']:
                                self.__tela_usuario_verificador.close()
                                return [usuario, email[0]]
                        raise NomeInvalidoException
                    else:
                        self.__tela_usuario_verificador.close()
                        break
                except NomeInvalidoException as e:
                    self.__tela_usuario_verificador.show_message('Aviso', str(e))
                    self.__tela_usuario_verificador.close()

    def informar_dados_usuario(self):
        if len(self.__usuariodao.get_all()) == 0:
            self.__tela_usuario.show_message("Aviso!", "Não existem usuarios cadastrados! "
                                             "Por favor cadastre pelo menos um")
        else:
            email = self.__tela_usuario_verificador.open()
            if email[0] == 'Enviar':
                try:
                    if "@" not in email[1]['email']:
                        raise EmailInvalidoException
                    entrada = email[1]['email'].split("@")
                    if entrada[1] != "gmail.com":
                        raise EmailInvalidoException
                    lista_comunidades = []
                    for usuario in self.__usuariodao.get_all():
                        if usuario.email == email[1]['email']:
                            for comunidade in usuario.comunidades:
                                lista_comunidades.append(comunidade.nome)
                            if len(lista_comunidades) == 0:
                                lista_comunidades = 'Nenhuma'
                            else:
                                lista_comunidades = "\n".join(lista_comunidades)
                            self.__tela_usuario.show_message(usuario.nome.upper(), "Nome do Usuario: " + usuario.nome +
                                                             "\nCredito do usuario: " + str(usuario.saldo)
                                                             + "\nEmail do usuario: " + usuario.email +
                                                             "\nIdade do usuario: " + str(usuario.idade) +
                                                             "\nComunidades que participa:\n " +
                                                             lista_comunidades)
                except EmailInvalidoException:
                    self.__tela_usuario.show_message('Aviso', 'Formato de email invalido ou email não '
                                                     'existe! Um email valido segue o padrao: exemplo@gmail.com')
            else:
                self.__tela_usuario_verificador.show_message("Aviso", "Processo Cancelado")

    def credita(self):
        if len(self.__usuariodao.get_all()) == 0:
            self.__tela_usuario.show_message('Aviso', 'Não existem usuarios cadastrados!'
                                             'Por favor, cadastre pelo menos um')
        else:
            usuario = self.get_usuario_by_email()
            if usuario is not None:
                while True:
                    if usuario[1] == 'Enviar':
                        try:
                            valor = self.__tela_usuario_credita.open()
                            if valor[0] == 'Enviar':
                                if float(valor[1]['valor']) > 500 or float(valor[1]['valor']) < 1: 
                                    raise ValueError
                                usuario[0].credite(float(valor[1]['valor']))
                                self.__usuariodao.add(usuario[0].id, usuario[0])
                                self.__tela_usuario_credita.close()
                                break
                            else:
                                self.__tela_usuario.show_message("Aviso", "Processo Cancelado")
                                self.__tela_usuario_credita.close()
                                break
                        except ValueError:
                            self.__tela_usuario.show_message('Erro!', 'Digite um valor entre 1 e 500')
                    else:
                        self.__tela_usuario.show_message("Aviso", "Processo Cancelado")
                        break
            else:
                self.__tela_usuario.show_message("Aviso", "Processo Cancelado")

    def cartao_de_credito(self):
        if len(self.__usuariodao.get_all()) == 0:
            self.__tela_usuario.show_message("Aviso!", "Nao existem usuarios cadastrados!"
                                                       "Cadastre ao menos um para fazer um"
                                                       "cartão!")
        else:
            while True:
                try:
                    dados = self.__tela_usuario_verifica_senha.open()
                    if dados[0] == 'Submit':
                        emails = self.lista_emails_usuarios()
                        if dados[1]['email'] not in emails:
                            raise EmailInvalidoException
                        usuario_obj = None
                        for usuario in self.__usuariodao.get_all():
                            if usuario.email == dados[1]['email'] and usuario.senha == dados[1]['senha']:
                                usuario_obj = usuario
                                break
                        if usuario_obj is None:
                            raise SenhaInvalidaException
                        self.__tela_usuario_verifica_senha.close()
                        self.__controlador_cartao_de_credito.abre_tela(usuario_obj)
                        break
                    else:
                        self.__tela_usuario.show_message("Aviso", "Processo cancelado")
                        self.__tela_usuario_verifica_senha.close()
                        break
                except EmailInvalidoException as e:
                    self.__tela_usuario.show_message("Aviso", str(e))
                except SenhaInvalidaException as e:
                    self.__tela_usuario.show_message("Aviso", str(e))

    def voltar(self):
        self.__continua_nesse_menu = False

    @property
    def usuarios(self):
        return self.__usuariodao.get_all()

    @property
    def dao(self):
        return self.__usuariodao

    def lista_emails_usuarios(self):
        lista_emails = []
        for usuario in self.__usuariodao.get_all():
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
