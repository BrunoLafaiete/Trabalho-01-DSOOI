from limite.tela_abstrata import TelaAbstrata
from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.desenvolvedora_invalida_exception import DesenvolvedoraInvalidaException
import PySimpleGUI as sg


class TelaJogo(TelaAbstrata):
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
        layout = [[sg.Button('Cadastrar um novo jogo', key=1, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Alterar dados de um jogo', key=2, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Pegar dados de um jogo', key=3, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Listar jogos', key=4, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Remover um jogo', key=5, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Button('Voltar', key=0, size=('1000', '3'),
                            font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))]]
        self.__window = sg.Window("Jogos", size=('1000', '520'), element_justification='center',
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()

    '''def tela_opcoes(self):
        print("------JOGO------")
        print()
        print("1 - Cadastrar um novo jogo")
        print("2 - Alterar dados do jogo")
        print("3 - Pegar dados do jogo")
        print("4 - Listar jogos")
        print("5 - Remover um jogo")
        print("0 - Voltar")
        print()
        opcao_escolhida = self.le_num_int("Escolha uma opção: ", [0, 1, 2, 3, 4, 5])
        return opcao_escolhida'''

    def cadastrar_jogo(self, jogos, desenvolvedoras):
        nomes_desenvolvedoras = []
        for desenvolvedora in desenvolvedoras:
            nomes_desenvolvedoras.append(desenvolvedora.nome)
        print("-----CADASTRAR UM JOGO-----")
        while True:
            nome = input("Nome: ")
            try:
                for jogo in jogos:
                    if jogo.nome == nome:
                        raise NomeInvalidoException
                break
            except NomeInvalidoException as e:
                print(e)
        while True:
            print("Desenvolvedoras disponiveis: " + self.le_lista(nomes_desenvolvedoras))
            desenvolvedora_str = input("Desenvolvedora: ")
            desenvolvedora_existe = False
            try:
                for desenvolvedora in desenvolvedoras:
                    if desenvolvedora.nome == desenvolvedora_str:
                        desenvolvedora_existe = True
                        obj_desenvolvedora = desenvolvedora
                        break
                if desenvolvedora_existe is False:
                    raise DesenvolvedoraInvalidaException
                break
            except DesenvolvedoraInvalidaException as e:
                print(e)

        genero = input("Genero: ")
        while True:
            faixa_etaria = input("Faixa etaria (0 ate 18): ")
            try:
                faixa_etaria = int(faixa_etaria)
                if faixa_etaria > 18 or faixa_etaria < 0:
                    raise ValueError
                break
            except ValueError:
                print("Selecione um valor inteiro valido")

        while True:
            preco = input("Preco (0 ate 10000): ")
            try:
                preco = float(preco)
                if preco > 10000 or preco < 0:
                    raise ValueError
                break
            except ValueError:
                print("Selecione um valor valido")

        return {"nome": nome, "desenvolvedora": obj_desenvolvedora, "genero": genero,
                "faixa etaria": faixa_etaria, "preco": preco}

    def alterar_jogo(self, jogos, desenvolvedoras, nome_antigo):
        nomes_desenvolvedoras = []
        for desenvolvedora in desenvolvedoras:
            nomes_desenvolvedoras.append(desenvolvedora.nome)
        print("-----ALTERAR DADOS-----")
        while True:
            nome = input("Nome: ")
            try:
                for jogo in jogos:
                    if jogo.nome == nome and nome != nome_antigo:
                        raise NomeInvalidoException
                break
            except NomeInvalidoException as e:
                print(e)

        while True:
            print("Desenvolvedoras disponiveis: " + self.le_lista(nomes_desenvolvedoras))
            desenvolvedora_str = input("Desenvolvedora: ")
            desenvolvedora_existe = False
            try:
                for desenvolvedora in desenvolvedoras:
                    if desenvolvedora.nome == desenvolvedora_str:
                        desenvolvedora_existe = True
                        obj_desenvolvedora = desenvolvedora
                        break
                if desenvolvedora_existe is False:
                    raise DesenvolvedoraInvalidaException
                break
            except DesenvolvedoraInvalidaException as e:
                print(e)
        genero = input("Genero: ")
        while True:
            faixa_etaria = input("Faixa etaria (0 ate 18): ")
            try:
                faixa_etaria = int(faixa_etaria)
                if faixa_etaria > 18 or faixa_etaria < 0:
                    raise ValueError
                break
            except ValueError:
                print("Selecione um valor inteiro valido")

        while True:
            preco = input("Preco (0 ate 10000): ")
            try:
                preco = float(preco)
                if preco > 10000 or preco < 0:
                    raise ValueError
                break
            except ValueError:
                print("Selecione um valor valido")

        return {"nome": nome, "desenvolvedora": obj_desenvolvedora, "genero": genero,
                "faixa etaria": faixa_etaria, "preco": preco}

    def mostrar_jogo(self, dados_jogo):
        print("\nNome do jogo: ", dados_jogo["nome"])
        print("Desenvolvedora do jogo: ", dados_jogo["desenvolvedora"])
        print("Genero do jogo: ", dados_jogo["genero"])
        print("Faixa etaria do jogo: ", dados_jogo["faixa etaria"])
        print("Preço do jogo: ", str(dados_jogo["preco"]) + "\n")

    def escrever_nome(self, nomes_jogos):
        print("Jogos disponiveis: " + self.le_lista(nomes_jogos))
        nome = input("Nome do jogo: ")
        return nome
