from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaComunidade(TelaAbstrata):
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
        layout = [[sg.Text(' ', font=('Helvetica', 10))],
                  [sg.Button('Criar uma nova comunidade', key=1, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Adicionar um usuário a uma comunidade', key=2, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Excluir usuário de uma comunidade', key=3, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Buscar uma comunidade pelo nome', key=4, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Listar comunidades', key=5, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Altera comunidade', key=6, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Excluir comunidade', key=7, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Voltar', key=0, size=('1000', '2'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))]]
        self.__window = sg.Window("IsTeam's", size=('1000', '520'), element_justification='center',
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()

    def retorna_comunidade(self, dados_comunidade):
        print("Comunidade ", dados_comunidade["nome"])
        print("Descrição: ", dados_comunidade["descricao"])
        print("Número de membros: ", dados_comunidade["numero_participantes"])
        print()

    def encontrar_usuario(self):
        email_usuario = input("Digite o email do usuario: ")
        senha = input("Digite a senha do usuario: ")
        return {"email": email_usuario, "senha": senha}

    def remove_usuario(self):
        print("REMOVER USUARIO DA UMA COMUNIDADE")

    def add_usuario(self):
        print("ADICIONAR USUARIO NA UMA COMUNIDADE")

    def remove_comunidade(self):
        print("REMOVER COMUNIDADE")
