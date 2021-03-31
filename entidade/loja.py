class Loja:
    def __init__(self, jogos):
        self.__jogos = jogos
        self.__generos = []
        self.__desenvolvedoras = []
        for jogo in jogos:
            if jogo.genero not in self.__generos:
                self.__generos.append(jogo.genero)
            #if jogo.desenvolvedora.nome not in self.__desenvolvedoras:
             #   self.__desenvolvedoras.append(jogo.desenvolvedora.nome)

    @property
    def jogos(self):
        return self.__jogos

    @property
    def generos(self):
        return self.__generos
