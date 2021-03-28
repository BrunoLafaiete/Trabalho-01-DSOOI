#from limite.tela_abstrata import TelaAbstrata


class TelaDesenvolvedora:

    def tela_opcoes(self):
        print("------DESENVOLVEDORA------")
        print()
        print("1 - Cadastrar uma nova desenvolvedora")
        print("2 - Alterar dados de uma desenvolvedora")
        print("3 - Pegar dados de uma desenvolvedora")
        print("4 - Listar desenvolvedoras")
        print()
        opcao_escolhida = int(input("Escolha uma opção: "))
        return opcao_escolhida

    def cadastrar_desenvolvedora(self):
        print("-----CADASTRAR UMA DESENVOLVEDORA-----")
        nome = input("Nome: ")

        return nome

    def alterar_desenvolvedora(self):
        print("-----ALTERAR DADOS-----")
        print("Vamos buscar uma desenvolvedora para alterar...")
        nome_antigo = input("Nome do Jogo: ")
        return nome_antigo

        #return {"nome": nome, "desenvolvedora": desenvolvedora, "genero": genero,
        # "faixa etaria": faixa_etaria, "preco": preco}

    def mostrar_desenvolvedora(self, dados_desenvolvedora):
        print("Nome da desenvolvedora: ", dados_desenvolvedora["nome"])
        print("Jogos da desenvolvedora: ", dados_desenvolvedora["jogos"])
