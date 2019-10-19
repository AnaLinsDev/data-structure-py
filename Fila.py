from Node import No

class Fila: 
    def __init__ ( self, head = None):
        self._head = head
    def isEmpty(self):
        if self._head.get_dado() == None:
            return True
        else: return False
    def add(self, elem):
        elem.set_proximo(self._head)
        self._head = elem
        return elem.get_dado()
    def remove(self):
        p = self._head
        while p.get_proximo().get_proximo() != None: #penultimo 
            p = p.get_proximo()
        #print(p.get_dado())
        p.set_proximo(None)
    def sizef(self):
        p = self._head
        count = 0 
        while p.get_proximo() != None:
            count+=1
            p = p.get_proximo()
        count+=1
        return count
    def showhead(self):
        p = self._head
        while p.get_proximo() != None:
            p = p.get_proximo()
        return p.get_dado()

fil = Fila()
a= No('um')
b= No('dois')
c= No('tres')
fil.add(a)
fil.add(b)
fil.add(c)
print(fil.sizef()) #3
print(fil.showhead())  #um
fil.remove()
print(fil.showhead()) #dois
