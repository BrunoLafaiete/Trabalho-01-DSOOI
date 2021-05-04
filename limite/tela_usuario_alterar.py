from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaUsuarioAlteraDados(TelaAbstrata):
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
        layout = [[sg.Text('Por favor digite os dados solicitados', font=('Helvetica', 10))],
                  [sg.Text('Email: ', size=('17', '1'), font=('Helvetica', 10)),
                   sg.InputText(key='email')],
                  [sg.Text('Senha: ', size=('17', '1'), font=('Helvetica', 10)),
                   sg.InputText(key='senha')],
                  [sg.Text('Nome completo: ', size=('17', '1'), font=('Helvetica', 10)),
                   sg.InputText(key='nome')],
                  [sg.Text('Idade : ', size=('17', '1'), font=('Helvetica', 10)),
                   sg.InputText(key='idade')],
                  [sg.Button('Enviar', font=('Helvetica', 10)), sg.Button('Cancelar', font=('Helvetica', 10))]]
        self.__window = sg.Window("Cadastrar um usuário", element_justification='center',
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()