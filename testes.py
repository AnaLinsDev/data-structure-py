
from Node import No
from Cdados import Dadu
import time

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
            print(True)
        else: print(False)
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
        if self.length() == 1 :
            self._head.set_dado(None)
            print('Lista vazia')
        if index == 0:
            self._head = self._head.get_proximo()
        if index > self.length():
            print ( ' indice invalido ')
        else:
            p = self._head
            q = self._head.get_proximo()
            for i in range(index - 1):
                q = q.get_proximo()
                p = p.get_proximo()
            p.set_proximo(q.get_proximo())
            q.set_proximo(p)
    def ordenar(self):
        if self._head == None:
            print("Não da para ordenar!")
        while True:   #Crescente!
            p = self._head
            q = self._head.get_proximo()
            while p != None:
                while q != None:
                    if p.get_dado().get_ano() > q.get_dado().get_ano():
                        aux = p.get_dado()
                        p.set_dado(q.get_dado())
                        q.set_dado(aux)
                        break
                    p = q
                    q = p.get_proximo()
                p = p.get_proximo()
            return self.printar_all()

    def length(self):
        p =self._head
        count = 0
        while p.get_proximo() != None:
            p =p.get_proximo()
            count+=1
        return count
    def printar_all(self):
        p = self._head
        while(p.get_proximo() != None):
            print(p.get_dado().get_filmeeano())
            p = p.get_proximo()
mov0 = Dadu('filme0', 1000)
no0 = mov0
mov1 = Dadu('filme1', 1111)
no1 = mov1
mov2 = Dadu('filme2', 2222)
no2 = mov2
mov3 = Dadu('filme3', 3333)
no3 = mov3
lista =Lista()
lista.insert(0, no3)
lista.insert(1, no0)
lista.insert(2, no1)
lista.insert(3, no2)
lista.ordenar()

'''    def ordenar(self):
        p = self._head
        q = p.get_proximo()
        z = p
        while p.get_proximo() != None:
            while q != None:
                if z.get_dado().get_ano() > q.get_dado().get_ano():
                    z.set_proximo(q.get_proximo())
                    q.set_proximo(z.get_dado())
                    q = q.get_proximo().get_proximo()
                else:
                    z = z.get_proximo()
                    q = q.get_proximo()
            p = p.get_proximo()
        return self.printar_all()'''