from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaComunidadeAddUsuario(TelaAbstrata):

    def __init__(self):
        self.__window = None

    def open(self, lista_comunidades): # -> 'mostra_menu'
        self.tela_opcoes(lista_comunidades)
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return (button_key, values)

    def tela_opcoes(self, lista_comunidades):
        lista = lista_comunidades
        sg.theme('Reddit')
        layout = [[sg.Text('Por favor digite as informaçoes: ', font=('Helvetica', 10))],
                  [sg.Text('Email: ', size=(17, 1), font=('Helvetica', 10)),
                   sg.InputText(key='email')],
                  [sg.Text('Comunidades: ', size=(17, 1), font=('Helvetica', 10))],
                  [sg.Combo(lista, key='nome_comunidade')],
                  [sg.Button('Enviar', font=('Helvetica', 10)), sg.Button('Cancelar', font=('Helvetica', 10))]]
        self.__window = sg.Window("Cadastrar um jogo",
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()

