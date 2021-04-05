import string
from limite.tela_abstrata import TelaAbstrata
from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.senha_invalida_exception import SenhaInvalidaException
from excecoes.email_invalido_exception import EmailInvalidoException
from excecoes.idade_invalida_exception import IdadeInvalidaException
from excecoes.credito_invalido_exception import CreditoInvalidoException


class TelaUsuario(TelaAbstrata):

    def tela_opcoes(self):
        print()
        print("-----USUÁRIO-----")
        print("1 - Cadastrar um usuário")
        print("2 - Alterar dados do usuário")
        print("3 - Pegar dados de um usuário")
        print("4 - Listar usuários")
        print("5 - Adicionar crédito")
        print("0 - Voltar")
        opcao_escolhida = self.le_num_int("Escolha uma opção: ", [0, 1, 2, 3, 4, 5])
        print()
        return opcao_escolhida

    def cadastrar_usuario(self, usuarios):
        print("-----CADASTRAR UM USUÁRIO-----")
        while True:
            email = input("Email: ")
            try:
                for usuario in usuarios:
                    if usuario.email == email:
                        raise EmailInvalidoException
                if "@" not in email:
                    raise EmailInvalidoException
                else:
                    entrada = email.split("@")
                    if entrada[1] != "gmail.com":
                        raise EmailInvalidoException
                break
            except EmailInvalidoException as e:
                print(e)

        while True:
            senha = input("Senha: ")
            try:
                for digito in senha:
                    if digito not in string.printable:
                        raise SenhaInvalidaException
                break
            except SenhaInvalidaException as e:
                print(e)
                print("Caracteres validos: ", string.printable)

        while True:
            nome = input("Nome Completo: ")
            try:
                for digito in nome:
                    if digito not in string.ascii_letters and digito not in [" ", "  "]:
                        raise NomeInvalidoException
                break
            except NomeInvalidoException as e:
                print(e)

        while True:
            idade = input("Idade: ")
            try:
                idade = int(idade)
                if 0 > idade or 130 < idade:
                    raise IdadeInvalidaException
                break
            except IdadeInvalidaException as e:
                print(e)
            except ValueError:
                print("Insira um valor valido para a idade!")

        return {"email": email, "senha": senha, "nome": nome, "idade": idade}

    def verificar_email(self):
        while True:
            email = input("Digite seu email: ")
            try:
                if "@" not in email:
                    raise EmailInvalidoException
                else:
                    entrada = email.split("@")
                    if entrada[1] != "gmail.com":
                        raise EmailInvalidoException
                break
            except EmailInvalidoException as e:
                print(e)
        return email

    def buscar_pelo_email(self, usuarios):
        print()
        print("-----BUSCA USUÁRIO-----")
        while True:
            email = input("Digite o email do usuário que deseja buscar: ")
            try:
                for usuario in usuarios:
                    if usuario.email != email:
                        raise EmailInvalidoException
                if "@" not in email:
                    raise EmailInvalidoException
                else:
                    entrada = email.split("@")
                    if entrada[1] != "gmail.com":
                        raise EmailInvalidoException
                break
            except EmailInvalidoException as e:
                print(e)
        return email

    def devolve_dados_usuario(self, dados_usuario):
        print()
        print("-----DADOS DESSE USUÁRIO-----")
        print("Email: ", dados_usuario["email"], "|", "Créditos: ", dados_usuario["creditos"], "|",
              "Nome: ", dados_usuario["nome"], "|", "Idade: ", dados_usuario["idade"])
        print("Jogos: ", self.le_lista(dados_usuario["jogos"]))
        print("Comunidades: ", self.le_lista(dados_usuario["comunidades"]))
        print()

    def verificar_senha(self):
        while True:
            senha = input("Senha: ")
            try:
                for digito in senha:
                    if digito not in string.printable:
                        raise SenhaInvalidaException
                break
            except SenhaInvalidaException as e:
                print(e)
        return senha

    def alterar_usuario(self, usuarios, email_antigo):
        print("-----ALTERARANDO OS DADOS-----")
        while True:
            email = input("Novo email: ")
            try:
                for usuario in usuarios:
                    if usuario.email == email and usuario.email != email_antigo:
                        raise EmailInvalidoException
                if "@" not in email:
                    raise EmailInvalidoException
                else:
                    entrada = email.split("@")
                    if entrada[1] != "gmail.com":
                        raise EmailInvalidoException
                break
            except EmailInvalidoException as e:
                print(e)

        while True:
            senha = input("Senha: ")
            try:
                for digito in senha:
                    if digito not in string.printable:
                        raise SenhaInvalidaException
                break
            except SenhaInvalidaException as e:
                print(e)
                print("Caracteres validos: ", string.printable)

        while True:
            nome = input("Nome Completo: ")
            try:
                for digito in nome:
                    if digito not in string.ascii_letters:
                        raise NomeInvalidoException
                break
            except NomeInvalidoException as e:
                print(e)

        while True:
            idade = input("Idade: ")
            try:
                idade = int(idade)
                if 0 > idade or 130 < idade:
                    raise IdadeInvalidaException
                break
            except IdadeInvalidaException as e:
                print(e)
            except ValueError:
                print("Por favor insira uma idade valida")
        return {"email": email, "senha": senha, "nome": nome, "idade": idade}

    def listar_usuario(self, dados_usuario):
        print()
        print("Email do usuário: ", dados_usuario["email"], "|", "Nome do usuário: ", dados_usuario["nome"], "|",
              "Idade do usuário: ", dados_usuario["idade"])
        print()

    def tela_credita(self, usuarios):
        print()
        print("-----ADICIONAR CRÉDITOS IsTeam's-----")
        while True:
            email = input("Email do usuário a creditar: ")
            try:
                for usuario in usuarios:
                    if usuario.email != email:
                        raise EmailInvalidoException
                if "@" not in email:
                    raise EmailInvalidoException
                else:
                    entrada = email.split("@")
                    if entrada[1] != "gmail.com":
                        raise EmailInvalidoException
                break
            except EmailInvalidoException as e:
                print(e)

        while True:
            valor = float(input("Valor que deseja adicionar a conta: "))
            try:
                if 1 > valor or valor > 500:
                    raise CreditoInvalidoException
                break
            except CreditoInvalidoException as e:
                print(e)

        return {"email": email, "valor": valor}
