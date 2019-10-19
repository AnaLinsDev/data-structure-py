from Node import No

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
    def sizep(self):
        p = self._topo
        count = 0 
        while p.get_proximo() != None:
            count+=1
            p = p.get_proximo()
        return count
    def showtopo(self):
        return self._topo.get_dado()

pil = Pilha()
a= No('um')
b= No('dois')
c= No('tres')
pil.add(a)
pil.add(b)
pil.add(c)
print(pil.sizep())   #3
print(pil.showtopo())   #tres
pil.remove()
print(pil.showtopo())  #dois