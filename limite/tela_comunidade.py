from limite.tela_abstrata import TelaAbstrata
from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.descricao_invalida_exception import DescricaoInvalidaException
from excecoes.comunidade_invalida_exception import ComunidadeInvalidaException
import PySimpleGUI as sg


class TelaComunidade(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def open(self): # -> 'mostra_menu'
        self.tela_opcoes() 
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return (button_key)

    def tela_opcoes(self):
        sg.theme('Reddit')
        layout = [[sg.Button('Criar uma nova comunidade', key=1, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Adicionar um usuário a uma comunidade', key=2, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Excluir usuário de uma comunidade', key=3, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Buscar uma comunidade pelo nome', key=4, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Listar comunidades', key=5, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Altera comunidade', key=6, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Excluir comunidade', key=7, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Voltar', key=0, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))]]
        self.__window = sg.Window("IsTeam's", size=('1000', '520'), element_justification='center',
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()

    '''def tela_opcoes(self):
        print()
        print("-----COMUNIDADES DA IsTeam's-----")
        print("1 - Criar uma nova comunidade")
        print("2 - Adicionar um usuário a uma Comunidade")
        print("3 - Exluir usuario de uma Comunidade")
        print("4 - Buscar uma comunidade pelo nome")
        print("5 - Listar comunidades")
        print("6 - Altera comunidade")
        print("7 - Excluir Comunidade")
        print("0 - Voltar ")
        opcao_escolhida = self.le_num_int("Escolha uma opção: ", [0, 1, 2, 3, 4, 5, 6, 7])
        print()
        return opcao_escolhida

    def nova_comunidade(self, comunidades):
        print("-----NOVA COMUNIDADE-----")
        while True:
            nome = input("Nome da comunidade: ")
            try:
                for comunidade in comunidades:
                    if comunidade.nome == nome:
                        raise NomeInvalidoException
                for digito in nome:
                    if digito not in string.ascii_letters and digito not in [" ", "  "]:
                        raise NomeInvalidoException
                break
            except NomeInvalidoException as e:
                print(e)
        while True:
            descricao = input("Descrição: ")
            try:
                for digito in descricao:
                    if digito not in string.ascii_letters and digito not in ["-", ",", ".", ";", ":", " ", "  "]:
                        raise DescricaoInvalidaException
                break
            except DescricaoInvalidaException as e:
                print(e)

        return {"nome": nome, "descricao": descricao}

    def altera_comunidade(self, comunidades, nome_antigo):
        while True:
            nome = input("Novo nome da comunidade: ")
            try:
                for comunidade in comunidades:
                    if comunidade.nome == nome and comunidade.nome != nome_antigo:
                        raise NomeInvalidoException
                for digito in nome:
                    if digito not in string.ascii_letters and digito not in [" ", "  "]:
                        raise NomeInvalidoException
                break
            except NomeInvalidoException as e:
                print(e)
        while True:
            descricao = input("Nova descrição: ")
            try:
                for digito in descricao:
                    if digito not in string.ascii_letters and digito not in ["-", ",", ".", ";", ":", " ", "  "]:
                        raise DescricaoInvalidaException
                break
            except DescricaoInvalidaException as e:
                print(e)

        return {"nome": nome, "descricao": descricao}

    def mostra_comunidades(self, dados_comunidade):
        print("Comunidade ", dados_comunidade["nome"])
        print("Descrição: ", dados_comunidade["descricao"])
        print("Número de participantes: ", dados_comunidade["numero_usuarios"])
        print()

    def print_comunidades_ativas(self):
        print("COMUNIDADES ATIVAS")

    def busca_comunidade(self, comunidades, nomes_comunidade):
        print("BUSCAR UMA COMUNIDADE")
        while True:
            print("Comunidades ativas: " + self.le_lista(nomes_comunidade))
            nome = input("Digite o nome da comunidade: ")
            try:
                for comunidade in comunidades:
                    if comunidade.nome == nome:
                        return comunidade
                raise ComunidadeInvalidaException
            except ComunidadeInvalidaException as e:
                print(e)'''

    def retorna_comunidade(self, dados_comunidade):
        print("Comunidade ", dados_comunidade["nome"])
        print("Descrição: ", dados_comunidade["descricao"])
        print("Número de membros: ", dados_comunidade["numero_participantes"])
        print()

    def encontrar_usuario(self):
        email_usuario = input("Digite o email do usuario: ")
        senha = input("Digite a senha do usuario: ")
        return {"email": email_usuario, "senha": senha}

    def remove_usuario(self):
        print("REMOVER USUARIO DA UMA COMUNIDADE")

    def add_usuario(self):
        print("ADICIONAR USUARIO NA UMA COMUNIDADE")

    def remove_comunidade(self):
        print("REMOVER COMUNIDADE")