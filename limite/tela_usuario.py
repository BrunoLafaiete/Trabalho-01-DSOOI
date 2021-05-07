from limite.tela_abstrata import TelaAbstrata
'''from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.senha_invalida_exception import SenhaInvalidaException
from excecoes.email_invalido_exception import EmailInvalidoException
from excecoes.idade_invalida_exception import IdadeInvalidaException
from excecoes.credito_invalido_exception import CreditoInvalidoException'''
import PySimpleGUI as sg


class TelaUsuario(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def open(self):
        self.tela_opcoes()
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return (button_key)

    def tela_opcoes(self):
        sg.theme('Reddit')
        layout = [[sg.Button('Cadastrar um usuário', key=1, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Alterar dados do usuário', key=2, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Pegar dados de um usuário', key=3, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Listar usuários', key=4, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Adicionar crédito', key=5, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Cartao de crédito', key=6, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Voltar', key=0, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))]]
        self.__window = sg.Window("Aba do Usuário", size=('1000', '520'), element_justification='center',
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()
