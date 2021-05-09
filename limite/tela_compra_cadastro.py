from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaCompraCadastro(TelaAbstrata):

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
                  [sg.Text('Email do usuario: ', size=(17, 1),
                          font=('Helvetica', 10)), sg.InputText(key="email")],
                  [sg.Text('Senha: ', size=(17, 1),
                           font=('Helvetica', 10)), sg.InputText(key="senha")],
                  [sg.Text('Nome do Jogo: ', size=(17, 1),
                           font=('Helvetica', 10)), sg.InputCombo(nomes_jogos, size=(17, 1), key="jogo")],
                  [sg.Submit(font=('Helvetica', 10)), sg.Cancel(font=('Helvetica', 10))]]
        self.__window = sg.Window("Nova Compra",
                                  finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()

    def comfirmar_cartao(self):
        boolean = sg.popup_yes_no("Realizar a compra com o cartao de credito?")
        return True if boolean == "Yes" else False
