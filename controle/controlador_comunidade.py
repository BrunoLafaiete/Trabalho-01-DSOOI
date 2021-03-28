from limite.tela_comunidade import TelaComunidade
from entidade.comunidade import Comunidade

class ControladorComunidade:
    def __init__(self, controlador_sistema):
        self.__comunidades = []
        self.__tela_comunidade = TelaComunidade()
        self.__controlador_sistema = controlador_sistema
        self.__usuarios = []
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {1: self.cria_comunidade, 3: self.busca_comunidade_por_nome, 4: self.lista_comunidades,
                        0: self.retorna_menu_principal}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_comunidade.tela_opcoes()]()

    def cria_comunidade(self):
        dados_comunidade = self.__tela_comunidade.nova_comunidade()
        comunidade = Comunidade(dados_comunidade["nome"], dados_comunidade["descricao"])
        self.__comunidades.append(comunidade)
    
    '''def adiciona_usuario(self):
        pass'''
    
    def busca_comunidade_por_nome(self):
        nome_a_buscar = self.__tela_comunidade.busca_comunidade()
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

    def retorna_menu_principal(self):
        self.__continua_nesse_menu = False
