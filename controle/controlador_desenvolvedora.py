from entidade.desenvolvedora import Desenvolvedora
from limite.tela_desenvolvedora import TelaDesenvolvedora
from excecoes.nome_invalido_exception import NomeInvalidoException


class ControladorDesenvolvedora:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__desenvolvedoras = []
        self.__tela_desenvolvedora = TelaDesenvolvedora()
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {0: self.voltar, 1: self.cadastra_desenvolvedora, 2: self.alterar_desenvolvedora,
                        3: self.get_dados_desenvolvedora, 4: self.lista_desenvolvedoras, 5: self.remover_desenvolvedora}
        self.__continua_nesse_menu = True

        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_desenvolvedora.tela_opcoes()]()

    def cadastra_desenvolvedora(self):
        desenvolvedora = Desenvolvedora(self.__tela_desenvolvedora.cadastrar_desenvolvedora(self.__desenvolvedoras))

        self.__desenvolvedoras.append(desenvolvedora)

    def alterar_desenvolvedora(self):
        if len(self.__desenvolvedoras) == 0:
            self.__tela_desenvolvedora.mostra_mensagem_erro("Não existem desenvolvedoras disponiveis! "
                                                            "Por favor insira pelo menos uma")
        else:
            desenvolvedora = self.get_desenvolvedora_by_nome()
            nome_antigo = desenvolvedora.nome
            desenvolvedora.nome = self.__tela_desenvolvedora.alterar_desenvolvedora(self.__desenvolvedoras, nome_antigo)

    def lista_desenvolvedoras(self):
        if len(self.__desenvolvedoras) == 0:
            self.__tela_desenvolvedora.mostra_mensagem_erro("Não existem desenvolvedoras disponiveis! "
                                                            "Por favor insira pelo menos uma")
        else:
            for desenvolvedora in self.__desenvolvedoras:
                self.__tela_desenvolvedora.mostrar_desenvolvedora({"nome": desenvolvedora.nome,
                                                                   "jogos":
                                                                       self.jogos_desenvolvedora_str(desenvolvedora)})
            
    def voltar(self):
        self.__continua_nesse_menu = False

    def get_dados_desenvolvedora(self):
        if len(self.__desenvolvedoras) == 0:
            self.__tela_desenvolvedora.mostra_mensagem_erro("Não existem desenvolvedoras disponiveis! "
                                                            "Por favor insira pelo menos uma")
        else:
            desenvolvedora = self.get_desenvolvedora_by_nome()
            self.__tela_desenvolvedora.mostrar_desenvolvedora({"nome": desenvolvedora.nome,
                                                               "jogos": self.jogos_desenvolvedora_str(desenvolvedora)})

    def get_desenvolvedora_by_nome(self):
        while True:
            try:
                nome = self.__tela_desenvolvedora.escrever_nome(self.nomes_desenvolvedoras())
                for desenvolvedora in self.__desenvolvedoras:
                    if desenvolvedora.nome == nome:
                        return desenvolvedora
                raise NomeInvalidoException
            except NomeInvalidoException as e:
                self.__tela_desenvolvedora.mostra_mensagem_erro(e)

    def remover_desenvolvedora(self):
        if len(self.__desenvolvedoras) == 0:
            self.__tela_desenvolvedora.mostra_mensagem_erro("Não existem desenvolvedoras disponiveis! "
                                                            "Por favor insira pelo menos uma")
        else:
            desenvolvedora = self.get_desenvolvedora_by_nome()
            if len(desenvolvedora.jogos) > 0:
                self.__tela_desenvolvedora.mostra_mensagem_erro("Essa desenvolvedora tem jogos ligados a ela! "
                                                                "Por favor remova-os ou mude a desenvolvedora deles")
            else:
                self.__desenvolvedoras.remove(desenvolvedora)
    @property
    def desenvolvedoras(self):
        return self.__desenvolvedoras

    def nomes_desenvolvedoras(self):
        desenvolvedoras = []
        for desenvolvedora in self.__desenvolvedoras:
            desenvolvedoras.append(desenvolvedora.nome)
        return desenvolvedoras

    def jogos_desenvolvedora_str(self, desenvolvedora):
        jogos_list = []
        for jogo in desenvolvedora.jogos:
            jogos_list.append(jogo.nome)
        return jogos_list
