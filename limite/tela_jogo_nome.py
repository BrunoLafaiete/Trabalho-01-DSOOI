from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaJogoNome(TelaAbstrata):

    def __init__(self):
        self.__window = None

    def open(self, lista_nomes):  # -> 'mostra_menu'
        self.tela_opcoes(lista_nomes)
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return button_key, values

    def tela_opcoes(self, lista_nomes):
        sg.theme('Reddit')
        layout = [[sg.Text(" Jogos Disponiveis: " + " ,".join(lista_nomes))],
                  [sg.Text('Por favor selecione o jogo', font=('Helvetica', 10))],
                  [sg.InputCombo(lista_nomes, size=(17, 1))],
                  [sg.Submit(font=('Helvetica', 10)), sg.Cancel(font=('Helvetica', 10))]]
        self.__window = sg.Window("Jogos", element_justification='center',
                                  finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()