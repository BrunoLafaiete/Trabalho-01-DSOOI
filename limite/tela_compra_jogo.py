from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaCompraJogo(TelaAbstrata):

    def __init__(self):
        self.__window = None

    def open(self, nomes_jogos): # -> 'mostra_menu'
        self.tela_opcoes(nomes_jogos)
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return button_key, values

    def tela_opcoes(self, nomes_jogos):
        sg.theme('Reddit')
        layout = [[sg.Text('Por favor digite as informaçoes', font=('Helvetica', 10))],
                  [sg.Text('Nome do Jogo: ', size=(17, 1),
                           font=('Helvetica', 10)), sg.InputCombo(nomes_jogos, size=(17, 1), key="jogo")],
                  [sg.Submit(font=('Helvetica', 10)), sg.Cancel(font=('Helvetica', 10))]]
        self.__window = sg.Window("Busca por Jogo",
                                  finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()