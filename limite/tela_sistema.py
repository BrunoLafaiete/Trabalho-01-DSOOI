


class TelaSistema:
    def tela_inicial(self):
        print("----------------------------")
        print("----------IsTeam's----------")
        print("----------------------------")
        print("1 - Acessar os Jogos")
        print("2 - Acessar a Loja")
        print("3 - Compra")
        print("4 - Aba do Usuário")
        print("5 - Comunidades")
        print("6 - Desenvolvedoras")
        print("7 - Finalizar Sistema")
        print()
        opcao_escolhida = int(input("Escolha uma opção: "))
        return opcao_escolhida

    def ler_mensagem_erro(self, mensagem):
        print(mensagem)

