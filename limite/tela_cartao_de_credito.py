import string
import datetime
from excecoes.nome_invalido_exception import NomeInvalidoException
from excecoes.instituicao_invalida_exception import InstituicaoInvalidaException
from limite.tela_abstrata import TelaAbstrata


class TelaCartaoDeCredito(TelaAbstrata):

    def tela_opcoes(self):
        print()
        print("----CARTAO DE CREDITO----")
        print("1 - Cadastrar Cartao de Credito")
        print("2 - Alterar Cartao de Credito")
        print("3 - Excluir Cartao de Credito")
        print("4 - Retornar Cartao de Credito")
        print("0 - Voltar")
        opcao_escolhida = self.le_num_int("Escolha uma opção: ", [0, 1, 2, 3, 4])
        print()
        return opcao_escolhida

    def cadastra_cartao(self):
        print("CADASTRAR CARTAO DE CREDITO")
        while True:
            nome_portador = input("Nome do portador: ")
            try:
                for digito in nome_portador:
                    if digito not in string.ascii_letters and digito not in [" ", "  "]:
                        raise NomeInvalidoException
                break
            except NomeInvalidoException as e:
                print(e)
        instiuicoes_disponiveis = ["Visa", "MasterCard", "JCB"]
        while True:
            print("Instituicoes disponiveis: ", self.le_lista(instiuicoes_disponiveis))
            instituicao = input("Instituicao do cartao: ")
            try:
                if instituicao not in instiuicoes_disponiveis:
                    raise InstituicaoInvalidaException
                break
            except InstituicaoInvalidaException as e:
                print(e)
        while True:
            numero = input("Numero do cartao: ")
            try:
                int(numero)
                if len(numero) != 16:
                    raise ValueError
                break
            except ValueError:
                print("Numero invalido!")
        while True:
            validade = input("Validade do cartao(formato mes/ano, MM/AAAA)): ")
            try:
                mes, ano = map(int, validade.split("/"))
                if mes > 12 or mes < 1 or ano < datetime.date.today().year:
                    raise ValueError
                validade = datetime.date(month=mes, year=ano, day=1)
                break
            except ValueError:
                print("Insira uma data valida")
        while True:
            codigo_seguranca = input("Codigo de seguranca: ")
            try:
                int(codigo_seguranca)
                if len(codigo_seguranca) != 3:
                    raise ValueError
                break
            except ValueError:
                print("Insira um codigo de seguranca valido")

        return {"nome portador": nome_portador, "instituicao": instituicao, "numero cartao": numero,
                "validade": validade, "codigo seguranca": codigo_seguranca}

    def altera_cartao(self):
        print("ALTERAR CARTAO")
        while True:
            nome_portador = input("Nome do portador: ")
            try:
                for digito in nome_portador:
                    if digito not in string.ascii_letters and digito not in [" ", "  "]:
                        raise NomeInvalidoException
                break
            except NomeInvalidoException as e:
                print(e)
        instiuicoes_disponiveis = ["Visa", "MasterCard", "JCB"]
        while True:
            print("Instituicoes disponiveis: ", self.le_lista(instiuicoes_disponiveis))
            instituicao = input("Instituicao do cartao: ")
            try:
                if instituicao not in instiuicoes_disponiveis:
                    raise InstituicaoInvalidaException
                break
            except InstituicaoInvalidaException as e:
                print(e)
        while True:
            numero = input("Numero do cartao: ")
            try:
                int(numero)
                if len(numero) != 16:
                    raise ValueError
                break
            except ValueError:
                print("Numero invalido!")
        while True:
            validade = input("Validade do cartao(formato mes/ano, MM/AAAA)): ")
            try:
                mes, ano = map(int, validade.split("/"))
                if mes > 12 or mes < 1 or ano < datetime.date.today().year or ano > (datetime.date.today().year + 50):
                    raise ValueError
                validade = datetime.date(month=mes, year=ano, day=1)
                break
            except ValueError:
                print("Insira uma data valida")
        while True:
            codigo_seguranca = input("Codigo de seguranca: ")
            try:
                int(codigo_seguranca)
                if len(codigo_seguranca) != 3:
                    raise ValueError
                break
            except ValueError:
                print("Insira um codigo de seguranca valido")

        return {"nome portador": nome_portador, "instituicao": instituicao, "numero cartao": numero,
                "validade": validade, "codigo seguranca": codigo_seguranca}

    def mostra_cartao(self, dados):
        dados = dados
        print("Titular do cartao: ", dados["nome"])
        print("Instituicao: ", dados["instituicao"])
        print("Numero do cartao: ", dados["numero"])
        print("Validade: ", dados["validade"])
        print("Codigo: ", dados["codigo"])
