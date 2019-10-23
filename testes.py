from Node import No
from Cdados import Dadu

class Lista:
    def __init__(self, head = None):  #Construtor
        self._head = head
        self._size = 0

    def mostrar(self, index):  #Mostra de acordo com o index
        p = self._head
        for i in range(index):
            if p.get_proximo() != None:
                p = p.get_proximo()
        return print(p.get_dado().get_filmeeano())
    def isEmpty(self): #Vazia
        if self._head == None:
            return True
        else: return False
    def insert(self, index, elem): #Inserir
            if self._head == None:
                no = No(elem)
                no.set_proximo(None)
                self._head = no
            if index > self.length():
                print ( ' indice invalido ')
            else:
                no = No(elem)
                q = self._head
                for i in range(index -1):
                    if q.get_proximo() != None:
                        q = q.get_proximo()
                no.set_proximo(q.get_proximo())
                q.set_proximo(no)
    def remove(self,index): #Remover um item no indice
        if index == 0:
            self._head = self._head.get_proximo()
        if index > self.size():
            print ( ' indice invalido ')
        else:
            p = self._head
            q = self._head.get_proximo()
            for i in range(index - 1):
                q = q.get_proximo()
                p = p.get_proximo()
            p.set_proximo(q.get_proximo())
            q.set_proximo(p)

    def printar_all(self):
        p = self._head
        while (p.get_proximo() != None):
            print(p.get_dado().get_filmeeano())
            p = p.get_proximo()
    def show(self, index):
        p = self._head
        for i in range(index):
            p = p.get_proximo()
        return p
    def ordenar(self):
        q = self._head
        p = q.get_proximo()
        while p.get_proximo() != None:
            while q.get_proximo() != None:
                if p.get_dado().get_ano() > q.get_proximo().get_dado().get_ano():
                    p.set_proximo(q.get_proximo)
                    q.set_proximo(p.get_dado)
                if p.get_dado().get_ano() < q.get_proximo().get_dado().get_ano():
                    q.set_proximo(p.get_proximo)
                    p.set_proximo(q.get_dado)
        p = p.get_proximo()
    def length(self):
        p =self._head
        count = 0
        while p.get_proximo() != None:
            p =p.get_proximo()
            count+=1
        return count
print("IFPB - Instituto Federal da Paraiba ")
print("-=-"*20)
mov0 = Dadu('PRIMEIRO', 2000)
no0 = mov0
mov2 = Dadu('TERCEIRO', 2002)
no2 = mov2
mov1 = Dadu('SEGUNDO', 2001)
no1 = mov1
lista =Lista()
lista.insert(0, no0)
lista.insert(0, no2)
lista.insert(0, no1)
lista.printar_all()
print(lista.length())
#lista.ordenar()
lista.printar_all()

