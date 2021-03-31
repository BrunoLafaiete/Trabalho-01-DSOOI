from limite.tela_abstrata import TelaAbstrata
from excecoes.nome_invalido_exception import NomeInvalidoException

class TelaDesenvolvedora(TelaAbstrata):

    def tela_opcoes(self):
        print("------DESENVOLVEDORA------")
        print()
        print("1 - Cadastrar uma nova desenvolvedora")
        print("2 - Alterar dados de uma desenvolvedora")
        print("3 - Pegar dados de uma desenvolvedora")
        print("4 - Listar desenvolvedoras")
        print("0 - Voltar")
        print()
        opcao_escolhida = self.le_num_int("Escolha uma opção: ", [0, 1, 2, 3, 4])
        return opcao_escolhida

    def cadastrar_desenvolvedora(self, desenvolvedoras):
        print("-----CADASTRAR UMA DESENVOLVEDORA-----")
        while True:
            try:
                nome = input("Nome: ")
                for desenvolvedora in desenvolvedoras:
                    if nome == desenvolvedora.nome:
                        raise NomeInvalidoException
                return nome
            except NomeInvalidoException as e:
                print(e)

    def alterar_desenvolvedora(self, desenvolvedoras, nome_antigo):
        print("-----ALTERAR DADOS-----")
        while True:
            try:
                nome = input("Nome: ")
                for desenvolvedora in desenvolvedoras:
                    if nome == desenvolvedora.nome and nome != nome_antigo:
                        raise NomeInvalidoException
                return nome
            except NomeInvalidoException as e:
                print(e)

    def mostrar_desenvolvedora(self, dados_desenvolvedora):
        print("\nNome da desenvolvedora: ", dados_desenvolvedora["nome"])
        print("Jogos da desenvolvedora: ", self.le_lista(dados_desenvolvedora["jogos"]) + "\n")

    def escrever_nome(self):
        nome = input("Nome da Desenvolvedora: ")
        return nome
