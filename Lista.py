from Node import No

class Lista:
    def __init__(self, head = None):
        self._head = head
        self._size = 0
    def mostrar(self, index):
        p = self._head
        for i in range(index):
            if p.get_proximo() != None:
                p = p.get_proximo()
        return print(p)
    def isEmpty(self): #Vazia
        return self._head == None
    def size(self): #Tamanho
        p = self._head
        count = 0
        while p.get_proximo() != None:
            count = count + 1
            p = p.get_proximo()
        return count
    def insert(self, index, elem):
            if index == 0:
                no = No(elem)
                no.set_proximo(self._head)
                self._head = no
            if index == self.lenght() - 1:
                no = No(elem)
                p = self._head
                while(p.get_proximo() != None):
                    p = p.get_proximo()
                p.set_proximo(no)
    def lenght(self):
        start = self._head
        size = 0
        while (start.get_proximo() != None):
            size += 1
            start = start.get_proximo()
        return size
    def printar_all(self):
        p = self._head
        while(p !=None):
            print(p)
            p = p.get_proximo()

p = No(2)
lista = Lista(p)
lista.insert(No(5), 0)
lista.insert(No(5), 0)
lista.insert(No(5), 0)
lista.printar_all()
print(lista.lenght())