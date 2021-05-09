from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaComunidadeAltera(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def open(self, comunidades_nome, tela): # -> 'mostra_menu'
        if tela == 'tela_1':
            self.tela_opcoes(comunidades_nome)
            button_key, values = self.__window.Read()
            if button_key is None:
                button_key = 0
            return (button_key, values)
        else:
            self.tela_opcoes2()
            button_key, values = self.__window.Read()
            if button_key is None:
                button_key = 0
            return (button_key, values)

    def tela_opcoes(self, comunidades_nome):
        sg.theme('Reddit')
        layout = [[sg.Text('Escolha a comunidade da qual deseja alterar', font=('Helvetica', 10))],
                  [sg.Listbox(comunidades_nome, size=(15, 3), key='comunidade')],
                  [sg.Button('Enviar', font=('Helvetica', 10)), sg.Button('Cancelar', font=('Helvetica', 10))]]
        self.__window = sg.Window("Alterar uma comunidade",
                                 finalize=True).Layout(layout)

    def tela_opcoes2(self):
        sg.theme('Reddit')
        layout = [[sg.Text('Por favor digite os dados solicitados', font=('Helvetica', 10))],
                  [sg.Text('Nome da comunidade: ', size=(17, 1), font=('Helvetica', 10)),
                   sg.InputText(key='nome')],
                  [sg.Text('Descricao da comunidade: ', size=(17, 1), font=('Helvetica', 10)),
                   sg.InputText(key='descricao')],
                  [sg.Button('Enviar', font=('Helvetica', 10)), sg.Button('Cancelar', font=('Helvetica', 10))]]
        self.__window = sg.Window("Alterar uma comunidade", element_justification='center',
                                  finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()