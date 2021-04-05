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
        opcao_escolhida = self.le_num_int("Escolha uma opção: ", [0, 1, 2, 3, 4, 5, 6, 7])
        return opcao_escolhida

    def ler_mensagem_erro(self, mensagem):
        print(mensagem)

    def le_num_int(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor invalido: Digite um valor numerico inteiro valido")
                if inteiros_validos:
                    print("Valores validos: ", inteiros_validos)
