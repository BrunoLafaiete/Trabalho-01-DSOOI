from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaDesenvolvedoraCadastro(TelaAbstrata):

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
        layout = [[sg.Text('Por favor digite um nome', font=('Helvetica', 10))],
                  [sg.Text('Nome: ', key='nome', size=(17, 1),
                          font=('Helvetica', 10)), sg.InputText()],
                  [sg.Submit(font=('Helvetica', 10)), sg.Cancel(font=('Helvetica', 10))]]
        self.__window = sg.Window("Cadastrar uma desenvolvedora", element_justification='center',
                                  finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()