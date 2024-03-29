from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaComunidadeVerificador(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def open(self):
        self.tela_opcoes()
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return (button_key, values)

    def tela_opcoes(self):
        sg.theme('Reddit')
        layout = [[sg.Text('Por favor digite o email do usuario', font=('Helvetica', 10))],
                  [sg.Text('Email: ', size=(17, 1), font=('Helvetica', 10)),
                   sg.InputText(key='email')],
                  [sg.Button('Enviar', font=('Helvetica', 10)), sg.Button('Cancelar', font=('Helvetica', 10))]]
        self.__window = sg.Window("Verificador", element_justification='center',
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()