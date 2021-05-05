from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaLojaGenero(TelaAbstrata):

    def __init__(self):
        self.__window = None

    def open(self, lista_generos): # -> 'mostra_menu'
        self.tela_opcoes(lista_generos)
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return button_key, values

    def tela_opcoes(self, lista_generos):
        sg.theme('Reddit')
        layout = [[sg.Text(" Generos Disponiveis: " + " ,".join(lista_generos))],
                  [sg.Text('Por favor selecione um genero', font=('Helvetica', 10))],
                  [sg.Combo(values=lista_generos, size=(17, 1))],
                  [sg.Submit(font=('Helvetica', 10)), sg.Cancel(font=('Helvetica', 10))]]
        self.__window = sg.Window("Generos", element_justification='center',
                                  finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()