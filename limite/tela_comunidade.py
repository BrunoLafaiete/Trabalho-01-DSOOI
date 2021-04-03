import string
from limite.tela_abstrata import TelaAbstrata
from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.descricao_invalida_exception import DescricaoInvalidaException
from excecoes.jogo_invalido_exception import JogoInvalidoException



class TelaComunidade(TelaAbstrata):

    def tela_opcoes(self):
        print()
        print("-----COMUNIDADES DA IsTeam's-----")
        print("1 - Criar uma nova comunidade")
        print("2 - Adicionar um usuário a uma Comunidade")
        print("3 - Buscar uma comunidade pelo nome")
        print("4 - Listar comunidades")
        print("0 - Voltar ")
        opcao_escolhida = self.le_num_int("Escolha uma opção: ", [0, 1, 2, 3, 4])
        print()
        return opcao_escolhida

    def nova_comunidade(self, comunidades, jogos):
        print("-----NOVA COMUNIDADE-----")
        while True:
            nome = input("Nome da comunidade: ")
            try:
                for comunidade in comunidades:
                    if comunidade.nome == nome:
                        raise NomeInvalidoException
                for digito in nome:
                    if digito not in string.ascii_letters and digito not in [" ", "  "]:
                        raise NomeInvalidoException
                break
            except NomeInvalidoException as e:
                print(e)
        while True:
            descricao = input("Descrição: ")
            try:
                for digito in descricao:
                    if digito not in string.ascii_letters and digito not in ["-", ",", ".", ";", ":", " ", "  "]:
                        raise DescricaoInvalidaException
                break
            except DescricaoInvalidaException as e:
                print(e)
        while True:
            nome_jogo = input("Essa comunidade falará do jogo: ")
            try:
                if nome_jogo not in jogos:
                    raise JogoInvalidoException
                break
            except JogoInvalidoException as e:
                print(e)

        return {"nome": nome, "descricao": descricao, "jogo": nome_jogo}

    def mostra_comunidades(self, dados_comunidade):
        print("Comunidade ", dados_comunidade["nome"])
        print("Descrição: ", dados_comunidade["descricao"])
        print("Número de participantes: ", dados_comunidade["numero_usuarios"])
        print()

    def print_comunidades_ativas(self):
        print("COMUNIDADES ATIVAS")

    def busca_comunidade(self, comunidades):
        print("BUSCAR UMA COMUNIDADE")
        while True:
            comunidade_a_buscar = input("Digite o nome da comunidade: ")
            try:
                nomes = []
                for comunidade in comunidades:
                    nomes.append(comunidade.nome)
                if comunidade_a_buscar not in nomes:
                    raise NomeInvalidoException
                break
            except NomeInvalidoException as e:
                print(e)

        return comunidade_a_buscar

    def retorna_comunidade(self, dados_comunidade):
        print("Comunidade ", dados_comunidade["nome"])
        print("Descrição: ", dados_comunidade["descricao"])
        print("Número de membros: ", dados_comunidade["numero_participantes"])
        print()
