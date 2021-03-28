


class TelaUsuario:

    def tela_opcoes(self):
        print()
        print("-----USUÁRIO-----")
        print("1 - Cadastrar um usuário")
        print("2 - Alterar dados do usuário")
        print("3 - Pegar dados de um usuário")
        print("4 - Listar usuários")
        print("5 - Adicionar crédito")
        print("0 - Voltar")
        opcao_escolhida = int(input("Escolha uma opção: "))
        print()
        return opcao_escolhida

    def cadastrar_usuario(self):
        print("-----CADASTRAR UM USUÁRIO-----")
        email = input("Email: ")
        senha = input("Senha: ")
        nome = input("Nome Completo: ")
        idade = input("Idade: ")
        return {"email": email, "senha": senha, "nome": nome, "idade": idade}

    def verificar_email(self):
        print("-----ALTERAR DADOS-----")
        print("Vamos buscar um usuásio para alterar...")
        email = input("Email: ")
        return email

    def buscar_pelo_email(self):
        print()
        print("-----BUSCA USUÁRIO-----")
        email = input("Digite o email do usuário que deseja buscar: ")
        return email

    def devolve_dados_usuario(self, dados_usuario):
        print()
        print("-----DADOS DESSE USUÁRIO-----")
        print("Email: ", dados_usuario["email"], "|", "Créditos: ", dados_usuario["creditos"], "|",
              "Nome: ", dados_usuario["nome"], "|", "Idade: ", dados_usuario["idade"])
        print()

    def verificar_senha(self):
        senha = input("Senha: ")
        return senha

    def alterar_usuario(self):
        print("-----ALTERARANDO OS DADOS-----")
        email = input("Email: ")
        senha = input("Senha: ")
        nome = input("Nome Completo: ")
        idade = input("Idade: ")
        return {"email": email, "senha": senha, "nome": nome, "idade": idade}

    def tela_senha_errada(self):
        print("VOCÊ DIGITOU UMA SENHA ERRADA!")

    def listar_usuario(self, dados_usuario):
        print()
        print("Email do usuário: ", dados_usuario["email"], "|", "Nome do usuário: ", dados_usuario["nome"], "|",
              "Idade do usuário: ", dados_usuario["idade"])
        print()

    def tela_credita(self):
        print()
        print("-----ADICIONAR CRÉDITOS IsTeam's-----")
        email = input("Email do usuário a creditar: ")
        valor = float(input("Valor que deseja adicionar a conta: "))
        return {"email": email, "valor": valor}