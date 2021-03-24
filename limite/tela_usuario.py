


class TelaUsuario:

    def tela_opcoes(self):
        print("-----USUÁRIO-----")
        print()
        print("1 - Cadastrar um novo usuário")
        print("2 - Alterar dados do usuário")
        print("3 - Pegar dados do usuário")
        print("4 - Listar usuários")
        print()
        opcao_escolhida = int(input("Escolha uma opção: "))
        return opcao_escolhida

    def cadastrar_usuario(self):
        print("-----CADASTRAR UM USUÁRIO-----")
        email = input("Email: ")
        senha = input("Senha: ")
        nome = input("Nome Completo: ")
        idade = input("Idade: ")
        return {"email": email, "senha": senha, "nome": nome, "idade": idade}

    def alterar_usuario(self):
        print("-----ALTERAR DADOS-----")
        print("Vamos buscar um usuásio para alterar...")
        usuario_existe = True
        '''usuario = ControladorUsuario()
        for i in usuario.self.__usuarios:
            if i.
            email = input("Email: ")
            senha = input("Senha: ")'''

        return {"email": email, "senha": senha}

    def mostrar_usuario(self, dados_usuario):
        print("Email do usuário: ", dados_usuario["email"])
        print("Nome do usuário: ", dados_usuario["nome"])
        print("Idade do usuário: ", dados_usuario["idade"])


