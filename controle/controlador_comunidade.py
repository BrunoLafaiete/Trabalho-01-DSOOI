from limite.tela_comunidade import TelaComunidade
from entidade.comunidade import Comunidade

class ControladorComunidade:
    def __init__(self, controlador_sistema):
        self.__comunidades = []
        self.__tela_comunidade = TelaComunidade()
        self.__controlador_sistema = controlador_sistema
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {1: self.cria_comunidade, 2: self.adicionar_usuario_a_comunidade, 3: self.busca_comunidade_por_nome, 4: self.lista_comunidades,
                        0: self.retorna_menu_principal}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_comunidade.tela_opcoes()]()

    def add_usuarios(self, usuarios):
        self.__usuarios = usuarios

    def cria_comunidade(self):
        dados_comunidade = self.__tela_comunidade.nova_comunidade(self.__comunidades)
        comunidade = Comunidade(dados_comunidade["nome"], dados_comunidade["descricao"])
        self.__comunidades.append(comunidade)

    def adicionar_usuario_a_comunidade(self):
        dados = self.__tela_comunidade.recebe_email(self.emails_usuarios(), self.nome_comunidades())
        for usuario in self.__usuarios:
            if usuario.email == dados["email"]:
                if usuario.senha == dados["senha"]:
                    for comunidade in self.__comunidades:
                        if comunidade.nome == dados["comunidade"]:
                            comunidade.usuarios.append(usuario)
                else:
                    self.__tela_comunidade.senha_errada()

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
                                                       "numero_usuarios": len(comunidade.usuarios)})
            else:
                self.__tela_comunidade.mostra_comunidades({"nome": comunidade.nome, "descricao": comunidade.descricao,
                                                           "numero_usuarios": len(comunidade.usuarios)})

    def existe_comunidade(self, name):
        for comunidade in self.__comunidades:
            if comunidade.nome == name:
                return True


    def retorna_menu_principal(self):
        self.__continua_nesse_menu = False

    @property
    def comunidades(self):
        return self.__comunidades

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
