from limite.tela_abstrata import TelaAbstrata


class TelaCompra(TelaAbstrata):

    def tela_opcoes(self):
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
        return {"email": email_usuario, "senha": senha}

    def compra_cartao(self):
        while True:
            print("Usar o cartao para a compra?")
            print("1- Sim")
            print("2 - Nao")
            resposta = self.le_num_int("Resposta: ", [1, 2])
            break
        if resposta == 1:
            resposta = True
        else:
            resposta = False
        return resposta
