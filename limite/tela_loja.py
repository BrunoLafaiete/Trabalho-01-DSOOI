from limite.tela_abstrata import TelaAbstrata
'''from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.desenvolvedora_invalida_exception import DesenvolvedoraInvalidaException'''
import PySimpleGUI as sg


class TelaLoja(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def open(self): # -> 'mostra_menu'
        self.tela_opcoes() 
        button_key, values = self.__window.Read()      #Fazar um método na tela_abstrata para o 'open'
        if button_key is None:                    
            button_key = 0
        return button_key

    def tela_opcoes(self):
        sg.theme('Reddit')
        layout = [[sg.Button('Listar jogos', key=1, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Procurar por genero', key=2, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Buscar por desenvolvedora', key=3, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Buscar por faixa etaria', key=4, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Buscar por preco', key=5, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))],
                  [sg.Button('Voltar', key=0, size=(1000, 3),
                            font=('Helvetica', 12), border_width=0, focus=(True, 'invisible'))]]
        self.__window = sg.Window("Loja", size=(1000, 520), element_justification='center',
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()
