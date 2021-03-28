

class TelaCompra:

    def tela_opcoes(self):
        print("-----COMPRAS-----")
        print("1 - Verificar os dados de uma compra")
        print("0 - Voltar")
        opcao_escolhida = int(input("Escolha um opção: "))
        return opcao_escolhida

    def verifica_compra(self):
        email = input("Digite o email do usuário que fez a compra: ")
        senha = input("Digite a senha desse usuário: ")
        identificador = input("Digite o identificador da compra: ")
        return {"email": email, "senha": senha, "idenrificador": identificador}

    def retorna_informacoes_compra(self, informacoes):
        print()
        print("DETALHES DA COMPRA")
        print("Jogo: ", informacoes["jogo"])
        print("Usuário: ", informacoes["usuario"])
        print("Data da compra: ", informacoes["data"])
