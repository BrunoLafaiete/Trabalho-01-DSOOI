from limite.tela_abstrata import TelaAbstrata
from excecoes.nome_invalido_exception import NomeInvalidoException
import PySimpleGUI as sg


class TelaDesenvolvedora(TelaAbstrata):
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
        layout = [[sg.Button('Cadastrar uma nova desenvolvedora', key=1, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Alterar dados de uma desenvolvedora', key=2, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Pegar dados de uma desenvolvedora', key=3, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Listar desenvolvedoras', key=4, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Remover uma desenvolvedora', key=5, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Voltar', key=0, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))]]
        self.__window = sg.Window("Desenvolvedoras", size=('1000', '520'), element_justification='center',
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()

    '''def tela_opcoes(self):
        print("------DESENVOLVEDORA------")
        print()
        print("1 - Cadastrar uma nova desenvolvedora")
        print("2 - Alterar dados de uma desenvolvedora")
        print("3 - Pegar dados de uma desenvolvedora")
        print("4 - Listar desenvolvedoras")
        print("5 - Remover uma desenvolvedora")
        print("0 - Voltar")
        print()
        opcao_escolhida = self.le_num_int("Escolha uma opção: ", [0, 1, 2, 3, 4, 5])
        return opcao_escolhida

    def cadastrar_desenvolvedora(self, desenvolvedoras):
        print("-----CADASTRAR UMA DESENVOLVEDORA-----")
        while True:
            try:
                nome = input("Nome: ")
                for desenvolvedora in desenvolvedoras:
                    if nome == desenvolvedora.nome:
                        raise NomeInvalidoException
                return nome
            except NomeInvalidoException as e:
                print(e)

    def alterar_desenvolvedora(self, desenvolvedoras, nome_antigo):
        print("-----ALTERAR DADOS-----")
        while True:
            try:
                nome = input("Nome: ")
                for desenvolvedora in desenvolvedoras:
                    if nome == desenvolvedora.nome and nome != nome_antigo:
                        raise NomeInvalidoException
                return nome
            except NomeInvalidoException as e:
                print(e)'''

    def mostrar_desenvolvedora(self, dados_desenvolvedora):
        print("\nNome da desenvolvedora: ", dados_desenvolvedora["nome"])
        print("Jogos da desenvolvedora: ", self.le_lista(dados_desenvolvedora["jogos"]) + "\n")

    def escrever_nome(self, nomes_desenvolvedoras):
        print("desenvolvedoras disponiveis: " + self.le_lista(nomes_desenvolvedoras))
        nome = input("Nome da Desenvolvedora: ")
        return nome
