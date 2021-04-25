from entidade.jogo import Jogo
from limite.tela_jogo import TelaJogo
from excecoes.nome_invalido_exception import NomeInvalidoException


class ControladorJogo:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogo = TelaJogo()
        self.__jogos = []
        self.__continua_nesse_menu = True
        self.__desenvolvedoras = None
        self.__compras = None

    def gerar_desenvolvedoras_e_compras(self, desenvolvedoras, compras):
        self.__desenvolvedoras = desenvolvedoras
        self.__compras = compras

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_jogo, 2: self.altera_jogo, 3: self.get_dados_jogo,
                        4: self.lista_jogos, 5: self.remover_jogo, 0: self.voltar}
        self.__continua_nesse_menu = True

        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_jogo.open()]()

    def cadastra_jogo(self):
        if len(self.__desenvolvedoras) == 0:
            self.__tela_jogo.show_message("Aviso!", "Não existem desenvolvedoras "
                                                    "disponiveis! Por favor insira pelo "
                                                    "menos uma antes de cadastrar um jogo ")
        else:
            dados_jogo = self.__tela_jogo.cadastrar_jogo(self.__jogos, self.__desenvolvedoras)
            jogo = Jogo(dados_jogo["nome"], dados_jogo["desenvolvedora"], dados_jogo["genero"],
                        dados_jogo["faixa etaria"], dados_jogo["preco"])

            self.__jogos.append(jogo)
            for desenvolvedora in self.__desenvolvedoras:
                if dados_jogo["desenvolvedora"] == desenvolvedora:
                    desenvolvedora.incluir_jogo(jogo)

    def lista_jogos(self):
        if len(self.__jogos) == 0:
            self.__tela_jogo.show_message("Aviso!", "Não existem jogos disponiveis! "
                                                    "Por favor insira pelo menos um")
        else:
            for jogo in self.__jogos:
                self.__tela_jogo.mostrar_jogo({"nome": jogo.nome, "desenvolvedora": jogo.desenvolvedora.nome,
                                               "genero": jogo.genero, "faixa etaria": jogo.faixa_etaria,
                                               "preco": jogo.preco})

    def altera_jogo(self):
        if len(self.__jogos) == 0:
            self.__tela_jogo.show_message("Aviso!", "Não existem jogos disponiveis! "
                                                    "Por favor insira pelo menos um")
        else:
            jogo = self.get_jogo_by_nome()
            nome_antigo = jogo.nome
            dados_jogo = self.__tela_jogo.alterar_jogo(self.__jogos, self.__desenvolvedoras, nome_antigo)
            jogo.nome = dados_jogo["nome"]
            jogo.genero = dados_jogo["genero"]
            jogo.preco = dados_jogo["preco"]
            jogo.faixa_etaria = dados_jogo["faixa etaria"]
            if dados_jogo["desenvolvedora"] != jogo.desenvolvedora:
                for desenvolvedora in self.__desenvolvedoras:
                    if desenvolvedora == jogo.desenvolvedora:
                        desenvolvedora.excluir_jogo(jogo)
                    elif dados_jogo["desenvolvedora"]:
                        desenvolvedora.incluir_jogo(jogo)
                jogo.desenvolvedora = dados_jogo["desenvolvedora"]

    def get_dados_jogo(self):
        if len(self.__jogos) == 0:
            self.__tela_jogo.show_message("Aviso!", "Não existem jogos disponiveis! "
                                                    "Por favor insira pelo menos um")
        else:
            jogo = self.get_jogo_by_nome()
            self.__tela_jogo.mostrar_jogo({"nome": jogo.nome, "desenvolvedora": jogo.desenvolvedora.nome,
                                           "genero": jogo.genero, "faixa etaria": jogo.faixa_etaria,
                                           "preco": jogo.preco})

    def remover_jogo(self):
        if len(self.__jogos) == 0:
            self.__tela_jogo.show_message("Aviso!", "Não existem jogos disponiveis! "
                                                    "Por favor insira pelo menos um")
        else:
            jogo = self.get_jogo_by_nome()
            jogo.desenvolvedora.excluir_jogo(jogo)
            for compra in jogo.compras:
                compra.usuario.remover_compra(compra)
                compra.usuario.remover_jogo(jogo)
            for compra in self.__compras:
                if compra.jogo == jogo:
                    self.__compras.remove(compra)
            self.__jogos.remove(jogo)

    def voltar(self):
        self.__continua_nesse_menu = False

    def get_jogo_by_nome(self):
        while True:
            try:
                nome = self.__tela_jogo.escrever_nome(self.nomes_jogo())
                for jogo in self.__jogos:
                    if jogo.nome == nome:
                        return jogo
                raise NomeInvalidoException
            except NomeInvalidoException:
                self.__tela_jogo.show_message("Erro", "Insira um jogo valido")

    @property
    def jogos(self):
        return self.__jogos

    def nomes_jogo(self):
        jogos = []
        for jogo in self.__jogos:
            jogos.append(jogo.nome)
        return jogos
