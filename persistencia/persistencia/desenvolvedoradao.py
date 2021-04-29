from persistencia.dao import DAO
from entidade.desenvolvedora import Desenvolvedora


class DesenvolvedoraDAO(DAO):
    def __init__(self):
        super().__init__('desenvolvedora.pkl')

    def add(self, key, desenvolvedora: Desenvolvedora):
        if (desenvolvedora is not None) and (isinstance(desenvolvedora.nome, str)):
            super().add(desenvolvedora.nome, desenvolvedora)

    def remove(self, desenvolvedora: Desenvolvedora):
        if (isinstance(desenvolvedora, Desenvolvedora)) and (desenvolvedora is not None):
            super().remove(desenvolvedora.nome)
