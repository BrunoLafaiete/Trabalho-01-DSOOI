from limite.tela_abstrata import TelaAbstrata
'''from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.senha_invalida_exception import SenhaInvalidaException
from excecoes.email_invalido_exception import EmailInvalidoException
from excecoes.idade_invalida_exception import IdadeInvalidaException
from excecoes.credito_invalido_exception import CreditoInvalidoException'''
import PySimpleGUI as sg


class TelaUsuarioCadastroDados(TelaAbstrata):
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
        layout = [[sg.Text('Por favor digite uma senha', font=('Helvetica', 12))],
                  [sg.Text('Senha: ', key='senha', size=('17', '1'),
                          font=('Helvetica', 12)), sg.InputText()],
                  [sg.Text('Nome completo: ', key='nome' ,size('17', '1'),
                          font=('Helvetica', 12)), sg.InputText()],
                  [sg.Text('Idade : ', key='idade' ,size('17', '1'),
                          font=('Helvetica', 12)), sg.InputText()],
                  [sg.Button('Voltar', key='voltar', font=('Helvetica', 12),
                            border_width='0', focus=(True, 'invisible'))]]
        self.__window = sg.Window("Cadastrar um usuário", element_justification='center',
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()
