from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaSistema(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def open(self): # -> 'mostra_menu'
        self.tela_opcoes() 
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return (button_key)

    def tela_opcoes(self):
        sg.theme('Reddit')
        layout = [[sg.Button('Acessar os Jogos', key=1, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Acessar a Loja', key=2, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Compra', key=3, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Aba do Usuário', key=4, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Comunidades', key=5, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Desenvolvedoras', key=6, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Finalizar Sistema', key=0, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))]]
        self.__window = sg.Window("IsTeam's", size=(1000, 520), element_justification='center',
                                  finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()
