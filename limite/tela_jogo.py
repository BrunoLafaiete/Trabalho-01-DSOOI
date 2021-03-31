from limite.tela_abstrata import TelaAbstrata
from excecoes.nome_invalido_exception import NomeInvalidoException


class TelaJogo(TelaAbstrata):

    def tela_opcoes(self):
        print("------JOGO------")
        print()
        print("1 - Cadastrar um novo jogo")
        print("2 - Alterar dados do jogo")
        print("3 - Pegar dados do jogo")
        print("4 - Listar jogos")
        print("0 - Voltar")
        print()
        opcao_escolhida = self.le_num_int("Escolha uma opção: ", [0, 1, 2, 3, 4])
        return opcao_escolhida

    def cadastrar_jogo(self, jogos):
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

        desenvolvedora = input("Desenvolvedora: ")
        genero = input("Genero: ")
        while True:
            faixa_etaria = input("Faixa etaria (0 ate 100): ")
            try:
                faixa_etaria = int(faixa_etaria)
                if faixa_etaria > 100 or faixa_etaria < 0:
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

        return {"nome": nome, "desenvolvedora": desenvolvedora, "genero": genero,
                "faixa etaria": faixa_etaria, "preco": preco}

    def alterar_jogo(self, jogos, nome_antigo):
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

        desenvolvedora = input("Desenvolvedora: ")
        genero = input("Genero: ")
        while True:
            faixa_etaria = input("Faixa etaria (0 ate 100): ")
            try:
                faixa_etaria = int(faixa_etaria)
                if faixa_etaria > 100 or faixa_etaria < 0:
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

        return {"nome": nome, "desenvolvedora": desenvolvedora, "genero": genero,
                "faixa etaria": faixa_etaria, "preco": preco}

    def mostrar_jogo(self, dados_jogo):
        print("\nNome do jogo: ", dados_jogo["nome"])
        print("Desenvolvedora do jogo: ", dados_jogo["desenvolvedora"])
        print("Genero do jogo: ", dados_jogo["genero"])
        print("Faixa etaria do jogo: ", dados_jogo["faixa etaria"])
        print("Preço do jogo: ", str(dados_jogo["preco"]) + "\n")

    def escrever_nome(self):
        nome = input("Nome do jogo: ")
        return nome
