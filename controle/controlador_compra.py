from limite.tela_compra import TelaCompra
from limite.tela_compra_cadastro import TelaCompraCadastro
from limite.tela_compra_jogo import TelaCompraJogo
from limite.tela_compra_usuario import TelaCompraUsuario
from entidade.compra import Compra
from excecoes.usuario_invalido_exception import UsuarioInvalidoException
from excecoes.saldo_insuficiente_exception import SaldoInsuficienteException
from excecoes.jah_possui_jogo_esception import JahPossuiJogoException
from excecoes.jogo_invalido_exception import JogoInvalidoException
from persistencia.compradao import CompraDAO


class ControladorCompra:
    def __init__(self, controlador_sistema):
        self.__compradao = CompraDAO()
        self.__tela_compra = TelaCompra()
        self.__tela_compra_cadastro = TelaCompraCadastro()
        self.__tela_compra_jogo = TelaCompraJogo()
        self.__tela_compra_usuario = TelaCompraUsuario()
        self.__controlador_sistema = controlador_sistema
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {1: self.comprar_jogo, 2: self.verifica_dados_compra, 3: self.historico_compras_usuario,
                        4: self.historico_compras_jogo, 5: self.listar_compras, 0: self.retorna_menu_principal}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_compra.open()]()

    def comprar_jogo(self):
        while True:
            try:
                dados = self.__tela_compra_cadastro.open(self.nome_jogos())
                if dados[0] == 'Submit':
                    usuario_obj = None
                    for usuario in self.__controlador_sistema.controlador_usuario.dao.get_all():
                        if usuario.email == dados[1]["email"] and usuario.senha == dados[1]["senha"]:
                            usuario_obj = usuario
                            break
                    if usuario_obj is None:
                        raise UsuarioInvalidoException
                    jogo_obj = None
                    for jogo in self.__controlador_sistema.controlador_jogo.dao.get_all():
                        if jogo.nome == dados[1]["jogo"]:
                            jogo_obj = jogo
                            break
                    if jogo_obj is None:
                        raise JogoInvalidoException
                    if usuario_obj is None:
                        raise UsuarioInvalidoException
                    if usuario_obj.cartao is not None:
                        comprar_por_cartao = self.__tela_compra_cadastro.comfirmar_cartao()
                    else:
                        comprar_por_cartao = False
                    if not comprar_por_cartao:
                        if jogo_obj.preco > usuario_obj.saldo:
                            raise SaldoInsuficienteException
                    if jogo_obj.faixa_etaria > usuario_obj.idade:
                        raise ValueError
                    if jogo_obj in usuario_obj.jogos:
                        raise JahPossuiJogoException
                    compra = Compra(jogo_obj, usuario_obj)
                    if not comprar_por_cartao:
                        usuario_obj.debite(jogo_obj.preco)
                    usuario_obj.incluir_jogo(jogo_obj)
                    self.__compradao.add(compra.id, compra)
                    self.__controlador_sistema.controlador_jogo.dao.add(jogo_obj.id, jogo_obj)
                    self.__controlador_sistema.controlador_usuario.dao.add(usuario_obj.id, usuario_obj)
                    self.__tela_compra.show_message("Sucesso", "Compra Realizada com sucesso")
                    self.__tela_compra_cadastro.close()
                    break
                else:
                    self.__tela_compra.show_message('Aviso', 'Processo Cancelado')
                    self.__tela_compra_cadastro.close()
                    break
            except ValueError:
                self.__tela_compra.show_message("Aviso!", "O Usuario nao possui a idade necessaria")
            except SaldoInsuficienteException as e:
                self.__tela_compra.show_message("Aviso!", str(e))
            except JahPossuiJogoException as e:
                self.__tela_compra.show_message("Aviso!", str(e))
            except UsuarioInvalidoException as e:
                self.__tela_compra.show_message("Aviso!", str(e))
            except JogoInvalidoException as e:
                self.__tela_compra.show_message("Aviso!", str(e))

    def historico_compras_usuario(self):
        usuario = self.get_usuario()
        if usuario is not None:
            lista_compras = list()
            for compra in usuario.compras:
                lista_compras.append("\nJogo: " + compra.jogo.nome + "\nValor: " + str(compra.jogo.preco) +
                                     "\nDesenvolvedora: " + compra.jogo.desenvolvedora.nome + "\nFaixa Etaria: " +
                                     str(compra.jogo.faixa_etaria) + "\nGenero: " + compra.jogo.genero +
                                     "\nData da compra: " + str(compra.data))
            self.__tela_compra.show_message("Historico de Compras", "\n".join(lista_compras))

    def verifica_dados_compra(self):
        usuario = self.get_usuario()
        if usuario is not None:
            jogo = self.get_jogo()
            if jogo is not None:
                for compra in self.__compradao.get_all():
                    if compra.usuario == usuario and compra.jogo == jogo:
                        self.__tela_compra.show_message("Compra", "\nUsuario: " + usuario.nome +
                                                        "\nData da compra: " + str(compra.data) + "Jogo: " + jogo.nome)
                        break

    def historico_compras_jogo(self):
        jogo = self.get_jogo()
        if jogo is not None:
            lista_compras = list()
            for compra in jogo.compras:
                lista_compras.append("\nUsuario: " + compra.usuario.nome + "\nData da compra: " + str(compra.data))
            self.__tela_compra.show_message("Historico de Compras", "\n".join(lista_compras))

    def listar_compras(self):
        lista_compras = list()
        for compra in self.__compradao.get_all():
            lista_compras.append("\nJogo: " + compra.jogo.nome + "\nUsuario: " + compra.usuario.nome +
                                 "\nData da compra: " + str(compra.data))
        self.__tela_compra.show_message("Historico de Compras", "\n".join(lista_compras))

    def get_usuario(self):
        while True:
            try:
                email = self.__tela_compra_usuario.open()
                if email[0] == 'Submit':
                    for usuario in self.__controlador_sistema.controlador_usuario.dao.get_all():
                        if usuario.email == email[1]['email']:
                            self.__tela_compra_usuario.close()
                            return usuario
                    raise UsuarioInvalidoException
                else:
                    self.__tela_compra.show_message('Aviso', 'Processo Cancelado')
                    self.__tela_compra_usuario.close()
                    return None
            except UsuarioInvalidoException as e:
                self.__tela_compra.show_message("Aviso!", str(e))
                self.__tela_compra_usuario.close()

    def get_jogo(self):
        while True:
            try:
                nome = self.__tela_compra_jogo.open(self.nome_jogos())
                if nome[0] == 'Submit':
                    for jogo in self.__controlador_sistema.controlador_jogo.dao.get_all():
                        if jogo.nome == nome[1]['jogo']:
                            self.__tela_compra_jogo.close()
                            return jogo
                    raise JogoInvalidoException
                else:
                    self.__tela_compra.show_message('Aviso', 'Processo Cancelado')
                    self.__tela_compra_jogo.close()
                    return None
            except JogoInvalidoException as e:
                self.__tela_compra.show_message("Aviso!", str(e))
                self.__tela_compra_jogo.close()

    def retorna_menu_principal(self):
        self.__continua_nesse_menu = False

    def nome_jogos(self):
        jogos = []
        for jogo in self.__controlador_sistema.controlador_jogo.dao.get_all():
            jogos.append(jogo.nome)
        return jogos

    @property
    def compras(self):
        return self.__compradao.get_all()

    @property
    def dao(self):
        return self.__compradao
