

class TelaCompra:

    def tela_opcoes(self):
        print("-----COMPRAS-----")
        print("1 - Comprar um jogo")
        print("2 - Verificar os dados de uma compra")
        print("3 - Histórico de compras de um usuário")
        print("0 - Voltar")
        opcao_escolhida = int(input("Escolha um opção: "))
        return opcao_escolhida

    def compra_by_nome(self):
        nome_jogo = input("Digite o nome do jogo que deseja comprar: ")
        usuario = input("Digite seu email (ou o email de um amigo se deseja presenteá-lo): ")
        return {"nome": nome_jogo, "usuario": usuario}

    def verifica_compra(self):
        email = input("Digite o email do usuário que fez a compra: ")
        senha = input("Digite a senha desse usuário: ")
        identificador = input("Digite o identificador da compra: ")
        return {"email": email, "senha": senha, "idenrificador": identificador}

    def historico_compras(self):
        email = input("Digite o email do usuário para verificarmos seu histórico: ")
        return email

    def retorna_historico_compras(self, dados_compra):
        print("-----HISTÓRICO DE COMPRAS-----")
        print("Jogo comprado: ", dados_compra["nome"])
        print("Preço: ", dados_compra["preco"])
        print("Desenvolvedora: ", dados_compra["desencolvedora"])
        print("Faixa etária: ", dados_compra["faixa_etaria"])
        print("Gênero: ", dados_compra["genero"])

    def retorna_informacoes_compra(self, informacoes):
        print()
        print("DETALHES DA COMPRA")
        print("Jogo: ", informacoes["jogo"])
        print("Usuário: ", informacoes["usuario"])
        print("Data da compra: ", informacoes["data"])
