


class TelaJogo:

    def tela_opcoes(self):
        print("------JOGO------")
        print()
        print("1 - Cadastrar um novo jogo")
        print("2 - Alterar dados do jogo")
        print("3 - Pegar dados do jogo")
        print("4 - Listar jogos")
        print()
        opcao_escolhida = int(input("Escolha uma opção: "))
        return opcao_escolhida

    def cadastrar_jogo(self):
        print("-----CADASTRAR UM JOGO-----")
        nome = input("Nome: ")
        desenvolvedora = input("Desenvolvedora: ")
        genero = input("Genero: ")
        faixa_etaria = input("Faixa etaria: ")
        preco = input("Preco: ")

        return {"nome": nome, "desenvolvedora": desenvolvedora, "genero": genero,
                "faixa etaria": int(faixa_etaria), "preco": float(preco)}

    def alterar_jogo(self):
        print("-----ALTERAR DADOS-----")
        print("Vamos buscar um jogo para alterar...")
        nome_antigo = input("Nome do Jogo: ")
        return nome_antigo

        #return {"nome": nome, "desenvolvedora": desenvolvedora, "genero": genero,
        # "faixa etaria": faixa_etaria, "preco": preco}

    def mostrar_jogo(self, dados_jogo):
        print("Nome do jogo: ", dados_jogo["nome"])
        print("Desenvolvedora do jogo: ", dados_jogo["desenvolvedora"])
        print("Genero do jogo: ", dados_jogo["genero"])
        print("Faixa etaria do jogo: ", dados_jogo["faixa etaria"])
        print("Preço do jogo: ", dados_jogo["preco"])
