from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaCartaoCadastra(TelaAbstrata):
    def _init_(self):
        self.__window = None

    def open(self): # -> 'mostra_menu'
        lista_bandeiras = ['mastercard', 'visa', 'elo']
        self.tela_opcoes(lista_bandeiras)
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return (button_key, values)

    def tela_opcoes(self, bandeiras):
        sg.theme('Reddit')
        layout = [[sg.Text('Por favor digite os dados solicitados', font=('Helvetica', 10))],
                  [sg.Text('Nome do portador: ', size=(17, 1), font=('Helvetica', 10)),
                   sg.InputText(key='nome_portador')],
                  [sg.Text('Numero do cartao: ', size=(17, 1), font=('Helvetica', 10)),
                   sg.InputText(key='numero')],
                  [sg.Text('Codigo de seguranca: ', size=(17, 1), font=('Helvetica', 10)),
                   sg.InputText(key='codigo')],
                  [sg.CalendarButton('validade_cartao'), sg.Input(key='data_validade')],
                  [sg.Text('Bandeiras', font=('Helvetica', 10))],
                  [sg.Listbox(bandeiras, size=(15, 3), key='bandeira')],
                  [sg.Button('Enviar', font=('Helvetica', 10)), sg.Button('Cancelar', font=('Helvetica', 10))]]
        self.__window = sg.Window("Alterar um cartao de credito", element_justification='center',
                                  finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()
