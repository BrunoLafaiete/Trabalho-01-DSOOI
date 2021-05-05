from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaLojaIdade(TelaAbstrata):

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
        layout = [[sg.Text('Por favor selecione uma faixa de idade: ', font=('Helvetica', 10))],
                  [sg.Slider(range=(0, 18), orientation='h', size=(34, 20),
                            default_value=0)],
                  [sg.Slider(range=(0, 18), orientation='h', size=(34, 20),
                             default_value=0)],
                  [sg.Submit(font=('Helvetica', 10)), sg.Cancel(font=('Helvetica', 10))]]
        self.__window = sg.Window("Busca Por Idade", finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()