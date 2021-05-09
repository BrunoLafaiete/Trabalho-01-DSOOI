from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaComunidadeDelUsuario(TelaAbstrata):

    def __init__(self):
        self.__window = None

    def open(self, comunidades_nome): # -> 'mostra_menu'
        self.tela_opcoes(comunidades_nome)
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return (button_key, values)

    def tela_opcoes(self, comunidades_nome):
        sg.theme('Reddit')
        layout = [[sg.Text('Escolha a comunidade da qual deseja remover o usuario', font=('Helvetica', 10))],
                  [sg.InputCombo(comunidades_nome, size=(15, 3), key='comunidade')],
                  [sg.Button('Enviar', font=('Helvetica', 10)), sg.Button('Cancelar', font=('Helvetica', 10))]]
        self.__window = sg.Window("Excluir um usuario da comunidade",
                                  finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()
