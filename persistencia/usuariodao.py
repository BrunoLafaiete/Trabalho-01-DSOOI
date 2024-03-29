from persistencia.dao import DAO
from entidade.usuario import Usuario


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuario.pkl')

    def add(self, key, usuario: Usuario):
        if (usuario is not None) and (isinstance(key, int)):
            super().add(key, usuario)

    def remove(self, usuario: Usuario):
        if (isinstance(usuario, Usuario)) and (usuario is not None):
            super().remove(usuario.id)
