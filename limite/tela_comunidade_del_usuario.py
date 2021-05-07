from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaComunidadeDelUsuario(TelaAbstrata):

    def __init__(self):
        self.__window = None

    def open(self, nomes_comunidades_usuario): # -> 'mostra_menu'
        self.tela_opcoes(nomes_comunidades_usuario)
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return (button_key, values)

    def tela_opcoes(self, nomes_comunidades_usuario):
        comunidades = nomes_comunidades_usuario
        sg.theme('Reddit')
        layout = [[sg.Text('Escolha a comunidade da qual deseja remover o usuario', font=('Helvetica', 10))],
                  [sg.Text('Comunidades: ', size=(20, 1), font=('Helvetica', 10))],
                  [sg.Combo(comunidades, key='nome_comunidade')],
                  [sg.Button('Enviar', font=('Helvetica', 10)), sg.Button('Cancelar', font=('Helvetica', 10))]]
        self.__window = sg.Window("Excluir um usuario da comunidade",
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()