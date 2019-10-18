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
    def __init__ ( self, topo = No()):
        self._topo = topo
    def isEmpty(self):
        if self._topo.get_dado() == None:
            return True
        else: return False
    def add(self, elem):
        elem.set_proximo(self._topo)
        self._topo = elem
    def remove(self):
        self._topo = self._topo.get_proximo()
   

    
class Fila: 
    def __init__ ( self, head = No()):
        self._head = head
    def isEmpty(self):
        if self._head.get_dado() == None:
            return True
        else: return False
    def add(self, elem):
        elem.set_proximo(self._head)
        self._head = elem
    def remove(self):
        self._head = self._head.get_proximo()
    





fil = Fila()
pil = Pilha()
print (pil.isEmpty())
print (fil.isEmpty())
a= No(1)
pil.add(a)
fil.add(a)
print (pil.isEmpty())
print (fil.isEmpty())
pil.remove()
fil.remove()
print (pil.isEmpty()) 
print (fil.isEmpty())


        



