from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaSistema(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Button('Acessar os Jogos', key=1)],
                  [sg.Button('Acessar a Loja', key=2)],
                  [sg.Button('Compra', key=3)],
                  [sg.Button('Aba do Usuário', key=4)],
                  [sg.Button('Comunidades', key=5)],
                  [sg.Button('Desenvolvedoras', key=6)],
                  [sg.Button('Finalizar Sistema', key=7)]]
        self.__window = sg.Window("IsTeam's").Layout(layout)

    def mostra_menu(self):
        self.init_components()
        button, values = self.__window.Read()
        if button is None:
            button = 0
        return (button)

    def close(self):
        self.__window.Close()

    def tela_inicial(self):
        print("----------------------------")
        print("----------IsTeam's----------")
        print("----------------------------")
        print("1 - Acessar os Jogos")
        print("2 - Acessar a Loja")
        print("3 - Compra")
        print("4 - Aba do Usuário")
        print("5 - Comunidades")
        print("6 - Desenvolvedoras")
        print("7 - Finalizar Sistema")
        print()
        opcao_escolhida = self.le_num_int("Escolha uma opção: ", [0, 1, 2, 3, 4, 5, 6, 7])
        return opcao_escolhida

    def ler_mensagem_erro(self, mensagem):
        print(mensagem)

    def le_num_int(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor invalido: Digite um valor numerico inteiro valido")
                if inteiros_validos:
                    print("Valores validos: ", inteiros_validos)
