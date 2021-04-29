from persistencia.dao import DAO
from entidade.comunidade import Comunidade


class ComunidadeDAO(DAO):
    def __init__(self):
        super().__init__('comunidade.pkl')

    def add(self, key, comunidade: Comunidade):
        if (comunidade is not None) and (isinstance(comunidade.nome, str)):
            super().add(comunidade.nome, Comunidade)

    def remove(self, comunidade: Comunidade):
        if (isinstance(comunidade, Comunidade)) and ( comunidade is not None):
            super().remove(comunidade.nome)
