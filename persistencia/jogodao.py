from persistencia.dao import DAO
from entidade.jogo import Jogo


class JogoDAO(DAO):
    def __init__(self):
        super().__init__('jogo.pkl')

    def add(self, key, jogo: Jogo):
        if (jogo is not None) and (isinstance(key, int)):
            super().add(key, jogo)

    def remove(self, jogo: Jogo):
        if (isinstance(jogo, Jogo)) and (jogo is not None):
            super().remove(jogo.id)
