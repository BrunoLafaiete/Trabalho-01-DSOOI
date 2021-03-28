


class TelaComunidade:

    def tela_opcoes(self):
        print()
        print("-----COMUNIDADES DA IsTeam's-----")
        print("1 - Criar uma nova comunidade")
        print("2 - Adicionar um usuário a uma Comunidade")
        print("3 - Buscar uma comunidade pelo nome")
        print("4 - Listar comunidades")
        opcao_escolhida = int(input("Escolha uma opção: "))
        print()
        return opcao_escolhida

    def nova_comunidade(self):
        print("-----NOVA COMUNIDADE-----")
        nome = input("Nome da comunidade: ")
        descricao = input("Descrição: ")
        return {"nome": nome, "descricao": descricao}

    def mostra_comunidades(self, dados_comunidade):
        print("Comunidade ", dados_comunidade["nome"])
        print("Descrição: ", dados_comunidade["descricao"])
        print("Número de participantes: ", dados_comunidade["numero_usuarios"])
        print()

    def print_comunidades_ativas(self):
        print("COMUNIDADES ATIVAS")

    def busca_comunidade(self):
        print("BUSCAR UMA COMUNIDADE")
        comunidade = input("Digite o nome da comunidade: ")
        return comunidade

    def retorna_comunidade(self, dados_comunidade):
        print("Comunidade ", dados_comunidade["nome"])
        print("Descrição: ", dados_comunidade["descricao"])
        print("Número de membros: ", dados_comunidade["numero_participantes"])
        print()

