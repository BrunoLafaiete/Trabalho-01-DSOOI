from entidade.desenvolvedora import Desenvolvedora
from limite.tela_desenvolvedora import TelaDesenvolvedora
from excecoes.nome_invalido_exception import NomeInvalidoException
from limite.tela_desenvolvedora_cadastro import TelaDesenvolvedoraCadastro
from limite.tela_desenvolvedora_nome import TelaDesenvolvedoraNome
from limite.tela_desenvolvedora_alterar import TelaDesenvolvedoraAlterar
from persistencia.desenvolvedoradao import DesenvolvedoraDAO


class ControladorDesenvolvedora:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__desenvolvedoradao = DesenvolvedoraDAO()
        self.__tela_desenvolvedora = TelaDesenvolvedora()
        self.__tela_desenvolvedora_cadastro = TelaDesenvolvedoraCadastro()
        self.__tela_desenvolvedora_nome = TelaDesenvolvedoraNome()
        self.__tela_desenvolvedora_alterar = TelaDesenvolvedoraAlterar()
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {0: self.voltar, 1: self.cadastra_desenvolvedora, 2: self.alterar_desenvolvedora,
                        3: self.get_dados_desenvolvedora, 4: self.lista_desenvolvedoras, 5: self.remover_desenvolvedora}
        self.__continua_nesse_menu = True

        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_desenvolvedora.open()]()
            self.__tela_desenvolvedora.close()

    def cadastra_desenvolvedora(self):
        while True:
            try:
                nome = self.__tela_desenvolvedora_cadastro.open()
                if nome[0] == 'Submit':
                    if len(nome[1][0]) == 0:
                        raise NomeInvalidoException
                    for desenvolvedora in self.__desenvolvedoradao.get_all():
                        if desenvolvedora.nome == nome[1][0]:
                            raise NomeInvalidoException
                    desenvolvedora = Desenvolvedora(nome[1][0])
                    self.__desenvolvedoradao.add(desenvolvedora.id, desenvolvedora)
                    self.__tela_desenvolvedora_cadastro.close()
                    break
                else:
                    self.__tela_desenvolvedora_cadastro.show_message('Aviso', 'Cadastro Cancelado')
                    break
            except NomeInvalidoException as e:
                self.__tela_desenvolvedora_cadastro.show_message('Aviso', str(e))
                self.__tela_desenvolvedora_cadastro.close()

    def alterar_desenvolvedora(self):
        if len(self.__desenvolvedoradao.get_all()) == 0:
            self.__tela_desenvolvedora.show_message("Aviso!", "Não existem desenvolvedoras disponiveis! "
                                                              "Por favor insira pelo menos uma")
        else:
            desenvolvedora_mudar = self.get_desenvolvedora_by_nome()
            if desenvolvedora_mudar is not None:
                nome_antigo = desenvolvedora_mudar.nome
                while True:

                    try:
                        novo_nome = self.__tela_desenvolvedora_alterar.open()
                        if novo_nome[0] == 'Submit':
                            for desenvolvedora in self.__desenvolvedoradao.get_all():
                                if desenvolvedora.nome == novo_nome[1][0] and novo_nome[1][0] != nome_antigo:
                                    raise NomeInvalidoException
                            desenvolvedora_mudar.nome = novo_nome[1][0]
                            self.__desenvolvedoradao.add(desenvolvedora_mudar.id, desenvolvedora_mudar)
                            for jogo in desenvolvedora_mudar.jogos:
                                self.__controlador_sistema.controlador_jogo.dao.add(jogo.id, jogo)
                            self.__tela_desenvolvedora.close()
                            break
                        else:
                            self.__tela_desenvolvedora_alterar.show_message('Aviso', 'Processo Cancelado')
                            self.__tela_desenvolvedora_alterar.close()
                            break
                    except NomeInvalidoException as e:
                        self.__tela_desenvolvedora_alterar.show_message('Aviso', str(e))
                        self.__tela_desenvolvedora_alterar.close()

    def lista_desenvolvedoras(self):
        if len(self.__desenvolvedoradao.get_all()) == 0:
            self.__tela_desenvolvedora.show_message("Aviso!", "Não existem desenvolvedoras disponiveis! "
                                                              "Por favor insira pelo menos uma")
        else:
            desenvolvedoras = list()
            for desenvolvedora in self.__desenvolvedoradao.get_all():
                desenvolvedoras.append(desenvolvedora.nome + "\nJogos: " +
                                       " ,".join(self.jogos_desenvolvedora_str(desenvolvedora)) + "\n")

            self.__tela_desenvolvedora.show_message("Listagem das Desenvolvedoras", "\n".join(desenvolvedoras))
            
    def voltar(self):
        self.__continua_nesse_menu = False

    def get_dados_desenvolvedora(self):
        if len(self.__desenvolvedoradao.get_all()) == 0:
            self.__tela_desenvolvedora.show_message("Aviso!", "Não existem desenvolvedoras disponiveis! "
                                                              "Por favor insira pelo menos uma")
        else:
            desenvolvedora = self.get_desenvolvedora_by_nome()
            if desenvolvedora is not None:
                self.__tela_desenvolvedora.show_message("Dados", (desenvolvedora.nome + "\nJogos: " +
                                                        " ,".join(self.jogos_desenvolvedora_str(desenvolvedora)) +
                                                                  "\n"))

    def get_desenvolvedora_by_nome(self):
        while True:
            try:
                nome = self.__tela_desenvolvedora_nome.open(self.nomes_desenvolvedoras())
                if nome[0] == 'Submit':
                    for desenvolvedora in self.__desenvolvedoradao.get_all():
                        if desenvolvedora.nome == nome[1][0]:
                            self.__tela_desenvolvedora_nome.close()
                            return desenvolvedora
                    raise NomeInvalidoException
                else:
                    self.__tela_desenvolvedora_nome.show_message('Aviso', 'Processo Cancelado')
                    self.__tela_desenvolvedora_nome.close()
                    return None
            except NomeInvalidoException as e:
                self.__tela_desenvolvedora.show_message('Aviso', str(e))
                self.__tela_desenvolvedora_nome.close()

    def remover_desenvolvedora(self):
        if len(self.__desenvolvedoradao.get_all()) == 0:
            self.__tela_desenvolvedora.show_message("Aviso!", "Não existem desenvolvedoras disponiveis! "
                                                              "Por favor insira pelo menos uma")
        else:
            desenvolvedora = self.get_desenvolvedora_by_nome()
            if desenvolvedora is not None:
                if len(desenvolvedora.jogos) > 0:
                    self.__tela_desenvolvedora.show_message("Aviso!", "Essa desenvolvedora tem jogos ligados a ela! "
                                                            "Por favor remova-os ou mude a desenvolvedora deles")
                else:
                    self.__desenvolvedoradao.remove(desenvolvedora)
                    self.__tela_desenvolvedora.show_message("Sucesso", "Desenvolvedora removida com sucesso")

    @property
    def desenvolvedoras(self):
        return self.__desenvolvedoradao.get_all()

    @property
    def dao(self):
        return self.__desenvolvedoradao

    def nomes_desenvolvedoras(self):
        desenvolvedoras = []
        for desenvolvedora in self.__desenvolvedoradao.get_all():
            desenvolvedoras.append(desenvolvedora.nome)
        return desenvolvedoras

    def jogos_desenvolvedora_str(self, desenvolvedora):
        jogos_list = []
        for jogo in desenvolvedora.jogos:
            jogos_list.append(jogo.nome)
        return jogos_list
