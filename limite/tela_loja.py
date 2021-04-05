from limite.tela_abstrata import TelaAbstrata
from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.desenvolvedora_invalida_exception import DesenvolvedoraInvalidaException


class TelaLoja(TelaAbstrata):

    def tela_opcoes(self):
        print("------LOJA------")
        print()
        print("1 - Listar jogos")
        print("2 - Procurar por genero")
        print("3 - Buscar por desenvolvedora")
        print("4 - Buscar por faixa etaria")
        print("5 - Buscar por preco")
        print("0 - Voltar")
        print()
        opcao_escolhida = self.le_num_int("Escolha a opcao: ", [0, 1, 2, 3, 4, 5])
        return opcao_escolhida

    def mostrar_jogo(self, dados_jogo):
        print("\nNome do jogo: ", dados_jogo["nome"])
        print("Desenvolvedora do jogo: ", dados_jogo["desenvolvedora"])
        print("Genero do jogo: ", dados_jogo["genero"])
        print("Faixa etaria do jogo: ", dados_jogo["faixa etaria"])
        print("Preço do jogo: ", dados_jogo["preco"], "\n")

    def conseguir_genero(self, generos_disponiveis):
        while True:
            try:
                print("Generos disponiveis:", self.le_lista(generos_disponiveis))
                genero = input("Escolha um genero: ")
                if genero in generos_disponiveis:
                    return genero
                raise NomeInvalidoException
            except NomeInvalidoException:
                print("Genero invalido! Selecione um genero valido")

    def conseguir_desenvolvedora(self, desenvolvedoras_disponiveis):
        print("Desenvolvedoras disponiveis:", self.le_lista(desenvolvedoras_disponiveis))
        while True:
            try:
                desenvolvedora = input("Escolha uma desenvolvedora valida: ")
                if desenvolvedora in desenvolvedoras_disponiveis:
                    return desenvolvedora
                raise DesenvolvedoraInvalidaException
            except DesenvolvedoraInvalidaException as e:
                print(e)


    def conseguir_preco(self):
        while True:
            print("Escolha a faixa de preco:")
            preco1 = input("Primeiro valor: ")
            preco2 = input("Segundo valor: ")
            try:
                preco1 = float(preco1)
                preco2 = float(preco2)
                return [preco1, preco2]
            except ValueError:
                print("Valor invalido: Digite um valor numerico valido!")

    def conseguir_idade(self):
        while True:
            print("Escolha a faixa de idade:")
            idade1 = input("Primeira idade: ")
            idade2 = input("Segunda idade: ")
            try:
                idade1 = int(idade1)
                idade2 = int(idade2)
                return [idade1, idade2]
            except ValueError:
                print("Valor invalido: Digite um valor numerico inteiro valido!")
