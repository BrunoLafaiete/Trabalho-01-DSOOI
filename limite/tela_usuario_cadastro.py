from limite.tela_abstrata import TelaAbstrata
'''from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.senha_invalida_exception import SenhaInvalidaException
from excecoes.email_invalido_exception import EmailInvalidoException
from excecoes.idade_invalida_exception import IdadeInvalidaException
from excecoes.credito_invalido_exception import CreditoInvalidoException'''
import PySimpleGUI as sg


class TelaUsuarioCadastro(TelaAbstrata):
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
        layout = [[sg.Text('Por favor digite um email', font=('Helvetica', 12))],
                  [sg.Text('Email: ', key='email', size=('17', '1'),
                          font=('Helvetica', 12)), sg.InputText()],
                  [sg.Button('Voltar', key='voltar', font=('Helvetica', 12),
                            border_width='0', focus=(True, 'invisible'))]]
        self.__window = sg.Window("Cadastrar um usuário", element_justification='center',
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()

    '''def cadastrar_usuario(self, usuarios):
        print("-----CADASTRAR UM USUÁRIO-----")
        while True:
            email = input("Email: ")
            try:
                for usuario in usuarios:
                    if usuario.email == email:
                        raise EmailInvalidoException
                if "@" not in email:
                    raise EmailInvalidoException
                else:
                    entrada = email.split("@")
                    if entrada[1] != "gmail.com":
                        raise EmailInvalidoException
                break
            except EmailInvalidoException as e:
                print(e)

        while True:
            senha = input("Senha: ")
            try:
                for digito in senha:
                    if digito not in string.printable:
                        raise SenhaInvalidaException
                break
            except SenhaInvalidaException as e:
                print(e)
                print("Caracteres validos: ", string.printable)

        while True:
            nome = input("Nome Completo: ")
            try:
                for digito in nome:
                    if digito not in string.ascii_letters and digito not in [" ", "  "]:
                        raise NomeInvalidoException
                break
            except NomeInvalidoException as e:
                print(e)

        while True:
            idade = input("Idade: ")
            try:
                idade = int(idade)
                if 0 > idade or 130 < idade:
                    raise IdadeInvalidaException
                break
            except IdadeInvalidaException as e:
                print(e)
            except ValueError:
                print("Insira um valor valido para a idade!")

        return {"email": email, "senha": senha, "nome": nome, "idade": idade}'''
