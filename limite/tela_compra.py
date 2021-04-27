from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaCompra(TelaAbstrata):
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
        layout = [[sg.Button('Comprar um jogo', key=1, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Verificar os dados de uma compra', key=2, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Histórico de compras de um usuário', key=3, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Histórico de compras de um jogo', key=4, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Listar compras', key=5, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Voltar', key=0, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))]]
        self.__window = sg.Window("Compras", size=('1000', '520'), element_justification='center',
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()

    '''def tela_opcoes(self):
        print("-----COMPRAS-----")
        print("1 - Comprar um jogo")
        print("2 - Verificar os dados de uma compra")
        print("3 - Histórico de compras de um usuário")
        print("4 - Histórico de compras de um jogo")
        print("5 - Listar Compras")
        print("0 - Voltar")
        opcao_escolhida = self.le_num_int("Escolha um opção: ", [0, 1, 2, 3, 4, 5])
        return opcao_escolhida

    def compra_by_nome(self):
        print("-----Realizar Compra-----")

    def verifica_compra(self):
        email = input("Digite o email do usuário que fez a compra: ")
        senha = input("Digite a senha desse usuário: ")
        identificador = input("Digite o identificador da compra: ")
        return {"email": email, "senha": senha, "idenrificador": identificador}

    def historico_compras_usuario(self):
        email = input("Digite o email do usuário para verificarmos seu histórico: ")
        return email

    def retorna_historico_compras(self, dados_compra):
        print("\n", dados_compra["data"])
        print("Jogo comprado: ", dados_compra["nome"])
        print("Preço: ", dados_compra["preco"])
        print("Desenvolvedora: ", dados_compra["desenvolvedora"])
        print("Faixa etária: ", dados_compra["faixa_etaria"])
        print("Gênero: ", dados_compra["genero"], "\n")

    def retorna_informacoes_compra(self, informacoes):
        print()
        print("DETALHES DA COMPRA")
        print("Jogo: ", informacoes["jogo"])
        print("Usuário: ", informacoes["usuario"])
        print("Data da compra: ", informacoes["data"])

    def encontrar_jogo(self, nome_jogos):
        print("Jogos disponiveis: ", self.le_lista(nome_jogos))
        nome_jogo = input("Digite o nome do jogo: ")
        return nome_jogo

    def encontrar_usuario(self):
        email_usuario = input("Digite o email do usuario: ")
        senha = input("Digite a senha do usuario: ")
        return {"email": email_usuario, "senha": senha}'''

    def compra_cartao(self):
        while True:
            print("Usar o cartao para a compra?")
            print("1 - Sim")
            print("2 - Nao")
            resposta = self.le_num_int("Resposta: ", [1, 2])
            break
        if resposta == 1:
            resposta = True
        else:
            resposta = False
        return resposta
