from limite.tela_comunidade import TelaComunidade
from entidade.comunidade import Comunidade

class ControladorComunidade:
    def __init__(self, controlador_sistema):
        self.__comunidades = []
        self.__tela_comunidade = TelaComunidade()
        self.__controlador_sistema = controlador_sistema
        self.__usuarios = []
        self.__continua_nesse_menu = True
        self.__jogos = None

    def abre_tela(self):
        lista_opcoes = {1: self.cria_comunidade, 3: self.busca_comunidade_por_nome, 4: self.lista_comunidades,
                        0: self.retorna_menu_principal}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_comunidade.tela_opcoes()]()

    def incluir_jogos(self, jogos):
        self.__jogos.append(jogos)

    def cria_comunidade(self):
        self.__controlador_sistema.jogos_pra_comunidade()
        dados_comunidade = self.__tela_comunidade.nova_comunidade(self.__comunidades, self.__jogos)
        comunidade = Comunidade(dados_comunidade["nome"], dados_comunidade["descricao"])
        comunidade.jogo = dados_comunidade["jogo"]
        self.__comunidades.append(comunidade)
    
    def busca_comunidade_por_nome(self):
        nome_a_buscar = self.__tela_comunidade.busca_comunidade(self.__comunidades)
        for comunidade in self.__comunidades:
            if comunidade.nome == nome_a_buscar:
                self.__tela_comunidade.retorna_comunidade({"nome": comunidade.nome, "descricao": comunidade.descricao, "numero_participantes": len(self.__usuarios)})

    def lista_comunidades(self):
        contador = 0
        for comunidade in self.__comunidades:
            contador += 1
            if contador == 1:
                self.__tela_comunidade.print_comunidades_ativas()
                self.__tela_comunidade.mostra_comunidades({"nome": comunidade.nome, "descricao": comunidade.descricao,
                                                       "numero_usuarios": len(self.__usuarios)})
            else:
                self.__tela_comunidade.mostra_comunidades({"nome": comunidade.nome, "descricao": comunidade.descricao,
                                                           "numero_usuarios": len(self.__usuarios)})

    def existe_comunidade(self, name):
        for comunidade in self.__comunidades:
            if comunidade.nome == name:
                return True


    def retorna_menu_principal(self):
        self.__continua_nesse_menu = False

    @property
    def comunidades(self):
        return self.__comunidades
