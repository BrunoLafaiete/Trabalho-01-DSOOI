from persistencia.dao import DAO
from entidade.desenvolvedora import Desenvolvedora


class DesenvolvedoraDAO(DAO):
    def __init__(self):
        super().__init__('desenvolvedora.pkl')

    def add(self, key, desenvolvedora: Desenvolvedora):
        if (desenvolvedora is not None) and (isinstance(key, int)):
            super().add(desenvolvedora.id, desenvolvedora)

    def remove(self, desenvolvedora: Desenvolvedora):
        if (isinstance(desenvolvedora, Desenvolvedora)) and (desenvolvedora is not None):
            super().remove(desenvolvedora.id)
