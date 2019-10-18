# Isso foi meu ctrl c + v do teu codigo, tentei rodar ele, mas n consegui, fiz umas alteraçoes, e continuei sem consegior( kk)
# mas to fazendo outro codigo do zero, pra tentar ser util, estao nos outros arquivos !!


class No:
    def __init__(self, dado = None, proximo = None):
        self._dado = dado
        self._proximo = proximo
    def get_dado(self):
        return self._dado
    def set_dado(self, novoDado):
        self._dado = novoDado
    def get_proximo(self):
        return self._proximo
    def set_proximo(self, outro):
        self._proximo = outro
    def size(self):
        return len(self._dado)
    def _str_(self):
        return "{}".format(self._dado)

class Pilha:
    def __init__(self, head = None):
        self._head = head
    def remove(self):
        self.head = self._head.get_proximo()
    def add(self, no):
        no.set_proximo(self._head)
        self._head = no

class Fila:
    def __init__(self, head = No()):
        self._head = head
        self._size = 0 
    def remove(self):
        self._head = self._head.get_proximo()
        self._size -= 1
    def add(self, no):
        p = self._head
        while(p.get_proximo() != None):
            p = p.get_proximo()
        p.set_proximo(no)
        self._size += 1
    def size(self):
        return self._size
    def insert(self, index,elem):
            if index == 0 :
                no = No(elem)
                no.set_proximo(self._head)
                self._head = no
    def Mostrar(self, index):
        p =self._head
        for i in range (index):
            if p.get_proximo() != None:
                p.get_proximo
            return print(p)
                

fil = Fila()
a = No(1)
b = No(2)
fil.add(a)
fil.add(b)
print(fil.insert(2,3))
print(fil.size())
fil.Mostrar(0)

