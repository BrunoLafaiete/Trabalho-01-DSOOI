from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaCompra(TelaAbstrata):
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
        layout = [[sg.Button('Comprar um jogo', key=1, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Verificar os dados de uma compra', key=2, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Histórico de compras de um usuário', key=3, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Histórico de compras de um jogo', key=4, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Listar compras', key=5, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Voltar', key=0, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))]]
        self.__window = sg.Window("Compras", size=(1000, 520), element_justification='center',
                                  finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()

