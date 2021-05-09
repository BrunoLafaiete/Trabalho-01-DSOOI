from persistencia.dao import DAO
from entidade.compra import Compra


class CompraDAO(DAO):
    def __init__(self):
        super().__init__('compra.pkl')

    def add(self, key, compra: Compra):
        if (compra is not None) and (isinstance(key, int)):
            super().add(key, compra)

    def remove(self, compra: Compra):
        if isinstance(compra, Compra) and (compra is not None):
            super().remove(compra.id)
