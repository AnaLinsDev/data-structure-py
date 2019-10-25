
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
    def mostrarano(self, index):  #Mostra de acordo com o index
        p = self._head
        a = self
        for i in range(index):
            if p.get_proximo() != None:
                p = p.get_proximo()
        return p.get_dado().get_ano()
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
        ordem = False
        while not ordem:
            ordem = True
            p = self._head
            q = p.get_proximo()
            while q.get_proximo() != None:
                if p.get_dado().get_ano() > q.get_dado().get_ano():
                    ordem = False
                    aux = p.get_dado()
                    p.set_dado(q.get_dado())
                    q.set_dado(aux)
                p = q
                q = q.get_proximo()

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
mov1 = Dadu('filme1', 1001)
no1 = mov1
mov2 = Dadu('filme2', 1002)
no2 = mov2
mov3 = Dadu('filme3', 1003)
no3 = mov3
mov4 = Dadu('filme4', 1004)
no4 = mov4
lista =Lista()
lista.insert(0, no4)
lista.insert(1, no0)
lista.insert(2, no3)
lista.insert(3, no1)
lista.insert(4, no2)
lista.printar_all()
print('\o/' * 15)
lista.ordenar()
lista.printar_all()

