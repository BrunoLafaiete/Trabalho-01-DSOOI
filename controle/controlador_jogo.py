from entidade.jogo import Jogo
from limite.tela_jogo import TelaJogo


class ControladorJogo:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogo = TelaJogo()
        self.__jogos = []
        self.__continua_nesse_menu = True


    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_jogo, 2: self.altera_jogo, 3: self.get_dados_jogo, 4: self.lista_jogos, 0: self.voltar}
        self.__continua_nesse_menu = True

        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_jogo.tela_opcoes()]()

    def cadastra_jogo(self):
        dados_jogo = self.__tela_jogo.cadastrar_jogo(self.__jogos)
        jogo = Jogo(dados_jogo["nome"], dados_jogo["desenvolvedora"], dados_jogo["genero"],
                    dados_jogo["faixa etaria"], dados_jogo["preco"])

        self.__jogos.append(jogo)

    def lista_jogos(self):
        for jogo in self.__jogos:
            self.__tela_jogo.mostrar_jogo({"nome": jogo.nome, "desenvolvedora": jogo.desenvolvedora,
                                           "genero": jogo.genero, "faixa etaria": jogo.faixa_etaria,
                                           "preco": jogo.preco})

    def altera_jogo(self):
        jogo = self.get_jogo_by_nome()
        nome_antigo = jogo.nome
        dados_jogo = self.__tela_jogo.alterar_jogo(self.__jogos, nome_antigo)
        jogo.nome = dados_jogo["nome"]
        jogo.genero = dados_jogo["genero"]
        jogo.preco = dados_jogo["preco"]
        jogo.faixa_etaria = dados_jogo["faixa etaria"]
        jogo.desenvolvedora = dados_jogo["desenvolvedora"]

    def get_dados_jogo(self):
        jogo = self.get_jogo_by_nome()
        self.__tela_jogo.mostrar_jogo({"nome": jogo.nome, "desenvolvedora": jogo.desenvolvedora, "genero": jogo.genero,
                                       "faixa etaria": jogo.faixa_etaria, "preco": jogo.preco})

    def voltar(self):
        self.__continua_nesse_menu = False

    def get_jogo_by_nome(self):
        nome = self.__tela_jogo.escrever_nome()
        for jogo in self.__jogos:
            if jogo.nome == nome:
                return jogo

    @property
    def jogos(self):
        return self.__jogos

