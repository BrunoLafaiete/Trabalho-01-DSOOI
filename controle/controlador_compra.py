from limite.tela_compra import TelaCompra
from entidade.compra import Compra
from excecoes.usuario_invalido_exception import UsuarioInvalidoException
from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.saldo_insuficiente_exception import SaldoInsuficienteException
from excecoes.jah_possui_jogo_esception import JahPossuiJogoException


class ControladorCompra:
    def __init__(self, controlador_sistema):
        self.__compras = []
        self.__tela_compra = TelaCompra()
        self.__controlador_sistema = controlador_sistema
        self.__continua_nesse_menu = True
        self.__usuarios = None
        self.__jogos = None

    def incluir_usuarios_e_jogos(self, jogos, usuarios):
        self.__jogos = jogos
        self.__usuarios = usuarios

    def abre_tela(self):
        lista_opcoes = {1: self.comprar_jogo, 2: self.verifica_dados_compra, 3: self.historico_compras_usuario,
                        4: self.historico_compras_jogo, 5: self.listar_compras, 0: self.retorna_menu_principal}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_compra.tela_opcoes()]()

    def comprar_jogo(self):
        self.__tela_compra.compra_by_nome()
        jogo = self.get_jogo()
        usuario = self.get_usuario()
        try:
            if jogo.preco > usuario.saldo:
                raise SaldoInsuficienteException
            if jogo.faixa_etaria > usuario.idade:
                raise ValueError
            if jogo in usuario.jogos:
                raise JahPossuiJogoException
            compra = Compra(jogo, usuario)
            usuario.debite(jogo.preco)
            self.__compras.append(compra)
        except ValueError:
            self.__tela_compra.mostra_mensagem_erro("O Usuario eh nao possui a idade necessaria")
        except SaldoInsuficienteException as e:
            self.__tela_compra.mostra_mensagem_erro(e)
        except JahPossuiJogoException as e:
            self.__tela_compra.mostra_mensagem_erro(e)


    def historico_compras_usuario(self):
        email = self.__tela_compra.historico_compras_usuario()
        while True:
            try:
                usuario_existe = False
                for usuario in self.__usuarios:
                    if usuario.email == email:
                        usuario_existe = True
                        usuario_para_checar = usuario
                        break
                if not usuario_existe:
                    raise UsuarioInvalidoException
                break
            except UsuarioInvalidoException as e:
                self.__tela_compra.mostra_mensagem_erro(e)

        self.__tela_compra.mostra_mensagem_erro("---Historico de Compras---")
        for compra in usuario_para_checar.compras:
            self.__tela_compra.retorna_historico_compras({"nome": compra.jogo.nome, "preco": compra.jogo.preco,
                                                          "desenvolvedora": compra.jogo.desenvolvedora.nome,
                                                          "faixa_etaria": compra.jogo.faixa_etaria,
                                                          "genero": compra.jogo.genero, "data": compra.data})

    def verifica_dados_compra(self):
        jogo = self.get_jogo()
        usuario = self.get_usuario()
        for compra in self.__compras:
            if compra.usuario == usuario and compra.jogo == jogo:
                self.__tela_compra.retorna_informacoes_compra({"jogo": compra.jogo.nome, "usuario": compra.usuario.nome, "data": compra.data})


    def historico_compras_jogo(self):
        jogo = self.get_jogo()
        self.__tela_compra.mostra_mensagem_erro("---Historico de Compras---")
        for compra in jogo.compras:
            self.__tela_compra.retorna_informacoes_compra({"jogo": compra.jogo.nome, "usuario": compra.usuario.nome,
                                                           "data": compra.data})


    def listar_compras(self):
        for compra in self.__compras:
            self.__tela_compra.retorna_informacoes_compra({"jogo": compra.jogo.nome, "usuario": compra.usuario.nome,
                                                           "data": compra.data})

    def retorna_menu_principal(self):
        self.__continua_nesse_menu = False

    def get_usuario(self):
        while True:
            dados_usuario = self.__tela_compra.encontrar_usuario()
            usuario_email = dados_usuario["email"]
            usuario_senha = dados_usuario["senha"]
            try:
                for usuario in self.__usuarios:
                    if usuario.senha == usuario_senha and usuario.email == usuario_email:
                        return usuario
                    raise UsuarioInvalidoException
            except UsuarioInvalidoException as e:
                self.__tela_compra.mostra_mensagem_erro(e)

    def get_jogo(self):
        while True:
            nome_jogo = self.__tela_compra.encontrar_jogo(self.nome_jogos())
            try:
                for jogo in self.__jogos:
                    if jogo.nome == nome_jogo:
                        return jogo
                    raise NomeInvalidoException
            except NomeInvalidoException as e:
                self.__tela_compra.mostra_mensagem_erro(e)

    def nome_jogos(self):
        jogos = []
        for jogo in self.__jogos:
            jogos.append(jogo.nome)
        return jogos
