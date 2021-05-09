from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaCartaoDeCredito(TelaAbstrata):
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
        layout = [[sg.Button('Cadastrar cartao de credito', key=1, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Alterar cartao de credito', key=2, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Excluir cartao de credito', key=3, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Retornar cartao de credito', key=4, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Voltar', key=0, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))]]
        self.__window = sg.Window("Cartao de credito", size=(1000, 520), element_justification='center',
                                  finalize=True).Layout(layout)

    def remover_cartao(self):
        boolean = sg.popup_yes_no("Remover o cartao de credito?")
        return True if boolean == "Yes" else False

    def close(self):
        self.__window.Close()
