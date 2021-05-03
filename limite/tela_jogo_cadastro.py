from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaJogoCadastro(TelaAbstrata):

    def __init__(self):
        self.__window = None

    def open(self, lista_desenvolvedoras): # -> 'mostra_menu'
        self.tela_opcoes(lista_desenvolvedoras)
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return button_key, values

    def tela_opcoes(self, lista_desenvolvedoras):
        sg.theme('Reddit')
        layout = [[sg.Text('Por favor digite as informaçoes: ', font=('Helvetica', 10))],
                  [sg.Text('Nome: ', key='nome', size=(17, 1),
                          font=('Helvetica', 10)), sg.InputText()],
                  [sg.Text('Desenvolvedora: ', key='desenvolvedora', size=(17, 1),
                           font=('Helvetica', 10)), sg.InputCombo(lista_desenvolvedoras, size=(17, 1))],
                  [sg.Text('Genero: ', key='genero', size=(17, 1),
                           font=('Helvetica', 10)), sg.InputText()],
                  [sg.Text('Faixa Etaria: ', key='faixa etaria', size=(17, 1),
                           font=('Helvetica', 10)), sg.Slider(range=(0, 18), orientation='h', size=(34, 20),
                            default_value=0)],
                  [sg.Text('Preco: ', key='preco', size=(17, 1),
                           font=('Helvetica', 10)), sg.InputText()],
                  [sg.Submit(font=('Helvetica', 10)), sg.Cancel(font=('Helvetica', 10))]]
        self.__window = sg.Window("Cadastrar um jogo",
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()
