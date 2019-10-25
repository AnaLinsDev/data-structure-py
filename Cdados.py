class Dadu:
    def __init__(self, filme=None, ano=None):
        self._filme = filme   
        self._ano = ano
    def get_filme(self):
        return self._filme
    def get_ano(self):
        return self._ano
    def set_filme(self, new):
         self._filme = new
    def set_ano(self, new):
        self._ano = new
    def set_filmeeano(self,newfil, newano):
        self._filme = newfil
        self._ano = newano
    def get_filmeeano(self):
        return f'{self._filme} de {self._ano}'
    
'''
mov0 = Dadu('filme0', '2000')
mov1 = Dadu('filme1', '2001')
mov2 = Dadu('filme2', '2002')
mov3 = Dadu('filme3', '2003')
mov4 = Dadu('filme4', '2004')
mov5 = Dadu('filme5', '2005')
mov6 = Dadu('filme6', '2006')
mov7 = Dadu('filme7', '2007')
'''




