from entidade.loja import Loja
from limite.tela_loja import TelaLoja
from limite.tela_loja_genero import TelaLojaGenero
from limite.tela_loja_desenvolvedora import TelaLojaDesenvolvedora
from limite.tela_loja_idade import TelaLojaIdade
from limite.tela_loja_preco import TelaLojaPreco
from excecoes.genero_invalido_exception import GeneroInvalidoException
from excecoes.desenvolvedora_invalida_exception import DesenvolvedoraInvalidaException


class ControladorLoja:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_loja = TelaLoja()
        self.__tela_loja_genero = TelaLojaGenero()
        self.__tela_loja_desenvolvedora = TelaLojaDesenvolvedora()
        self.__tela_loja_idade = TelaLojaIdade()
        self.__tela_loja_preco = TelaLojaPreco()
        self.__loja = None
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {1: self.listar_jogos, 2: self.buscar_por_genero, 3: self.buscar_por_desenvolvedora,
                        4: self.buscar_por_faixa_etaria, 5: self.buscar_por_preco, 0: self.voltar}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_loja.open()]()
            self.__tela_loja.close()

    def incluir_loja(self, jogos):
        self.__loja = Loja(jogos)

    def listar_jogos(self):
        lista_jogos = list()
        for jogo in self.__loja.jogos:
            lista_jogos.append("\nNome do Jogo: " + jogo.nome + "\nDesenvolvedora do jogo: " +
                               jogo.desenvolvedora.nome + "\nGenero do jogo: " + jogo.genero +
                               "\nFaixa etaria do jogo: " + str(jogo.faixa_etaria) + "\nPreço do jogo: " +
                               str(jogo.preco))
        self.__tela_loja.show_message("Listagem de Jogos", "\n".join(lista_jogos))

    def buscar_por_genero(self):
        while True:
            genero = self.__tela_loja_genero.open(self.__loja.generos)
            try:
                if genero[0] == 'Submit':
                    if genero[1][0] not in self.__loja.generos:
                        raise GeneroInvalidoException
                    lista_jogos = list()
                    for jogo in self.__loja.jogos:
                        if genero[1][0] == jogo.genero:
                            lista_jogos.append("\nNome do Jogo: " + jogo.nome + "\nDesenvolvedora do jogo: " +
                                               jogo.desenvolvedora.nome + "\nGenero do jogo: " + jogo.genero +
                                               "\nFaixa etaria do jogo: " + str(jogo.faixa_etaria) + "\nPreço do jogo: "
                                               + str(jogo.preco))
                    self.__tela_loja.show_message("Listagem de Jogos por Genero", "\n".join(lista_jogos))
                    self.__tela_loja_genero.close()
                    break
                else:
                    self.__tela_loja.show_message("Aviso", "Processo Cancelado")
                    self.__tela_loja_genero.close()
                    break
            except GeneroInvalidoException as e:
                self.__tela_loja.show_message("Aviso", str(e))
                self.__tela_loja_genero.close()

    def buscar_por_desenvolvedora(self):
        while True:
            desenvolvedora = self.__tela_loja_genero.open(self.__loja.desenvolvedoras)
            try:
                if desenvolvedora[0] == 'Submit':
                    if desenvolvedora[1][0] not in self.__loja.desenvolvedoras:
                        raise DesenvolvedoraInvalidaException
                    lista_jogos = list()
                    for jogo in self.__loja.jogos:
                        if desenvolvedora[1][0] == jogo.desenvolvedora.nome:
                            lista_jogos.append("\nNome do Jogo: " + jogo.nome + "\nDesenvolvedora do jogo: " +
                                               jogo.desenvolvedora.nome + "\nGenero do jogo: " + jogo.genero +
                                               "\nFaixa etaria do jogo: " + str(jogo.faixa_etaria) + "\nPreço do jogo: "
                                               + str(jogo.preco))
                    self.__tela_loja.show_message("Listagem de Jogos por Desenvolvedora", "\n".join(lista_jogos))
                    self.__tela_loja_genero.close()
                    break
                else:
                    self.__tela_loja.show_message("Aviso", "Processo Cancelado")
                    self.__tela_loja_genero.close()
                    break
            except DesenvolvedoraInvalidaException as e:
                self.__tela_loja.show_message("Aviso", str(e))
                self.__tela_loja_genero.close()

    def buscar_por_faixa_etaria(self):
        idades = self.__tela_loja_idade.open()
        if idades[0] == 'Submit':
            lista_jogos = list()
            for jogo in self.__loja.jogos:
                if min(int(idades[1][0]), int(idades[1][1])) <= jogo.faixa_etaria <= max(int(idades[1][0]),
                                                                                         int(idades[1][1])):
                    lista_jogos.append("\nNome do Jogo: " + jogo.nome + "\nDesenvolvedora do jogo: " +
                                       jogo.desenvolvedora.nome + "\nGenero do jogo: " + jogo.genero +
                                       "\nFaixa etaria do jogo: " + str(jogo.faixa_etaria) + "\nPreço do jogo: " +
                                       str(jogo.preco))
            self.__tela_loja.show_message("Listagem de Jogos por Idade", "\n".join(lista_jogos))
            self.__tela_loja_idade.close()
        else:
            self.__tela_loja.show_message("Aviso", "Processo Cancelado")
            self.__tela_loja_idade.close()

    def buscar_por_preco(self):
        while True:
            try:
                precos = self.__tela_loja_preco.open()
                if precos[0] == 'Submit':
                    lista_jogos = list()
                    for jogo in self.__loja.jogos:
                        if min(float(precos[1][0]), float(precos[1][1])) <= jogo.preco <= max(float(precos[1][0]),
                                                                                              float(precos[1][1])):
                            lista_jogos.append("\nNome do Jogo: " + jogo.nome + "\nDesenvolvedora do jogo: " +
                                               jogo.desenvolvedora.nome + "\nGenero do jogo: " + jogo.genero +
                                               "\nFaixa etaria do jogo: " + str(jogo.faixa_etaria) + "\nPreço do jogo: "
                                               + str(jogo.preco))

                    self.__tela_loja.show_message("Listagem de Jogos por Preco", "\n".join(lista_jogos))
                    self.__tela_loja_preco.close()
                    break
                else:
                    self.__tela_loja.show_message("Aviso", "Processo Cancelado")
                    self.__tela_loja_preco.close()
                    break
            except ValueError:
                self.__tela_loja.show_message("Erro", "Preços invalidos")
                self.__tela_loja_preco.close()

    def voltar(self):
        self.__continua_nesse_menu = False
