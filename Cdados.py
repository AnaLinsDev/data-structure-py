from Node import No

class Dadu:
    def __init__(self, musica, ano):
        self._musica = musica   
        self._ano = ano
    def get_musica(self):
        return self._musica
    def get_ano(self):
        return self._ano
    def set_musica(self, new):
         self._musica = new
    def set_ano(self, new):
        self._ano = new
    