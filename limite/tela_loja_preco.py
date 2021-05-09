from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaLojaPreco(TelaAbstrata):

    def __init__(self):
        self.__window = None

    def open(self): # -> 'mostra_menu'
        self.tela_opcoes()
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return button_key, values

    def tela_opcoes(self):
        sg.theme('Reddit')
        sg.theme('Reddit')
        layout = [[sg.Text('Por favor selecione uma faixa de preco: ', font=('Helvetica', 10))],
                  [sg.InputText()], [sg.InputText()],
                  [sg.Submit(font=('Helvetica', 10)), sg.Cancel(font=('Helvetica', 10))]]
        self.__window = sg.Window("Busca Por Preco", finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()
