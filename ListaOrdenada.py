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

    def ordenar(self): #Ordena de forma crescente!
        if self._head == None:
            print("Não dá para Ordenar!")
        else:
            ordem = False
            p = self._head
            q = p.get_proximo()
            while not ordem:
                ordem = True
                while q.get_proximo() != None: #Se o get proximo for None O whuile de cima será True.
                    if p.get_dado().get_ano() > q.get_dado().get_ano():
                        ordem = False #Isso vai fazer que volte para o outro while quando acabar esse
                        aux = p.get_dado()
                        p.set_dado(q.get_dado())
                        q.set_dado(aux)
                    p = q
                    q = q.get_proximo()
    def length(self): #Ver o tamanho
        p =self._head
        count = 0
        while p.get_proximo() != None:
            p =p.get_proximo()
            count+=1
        return count
    def printar_all(self): #Printa todos os elementos
        p = self._head
        while (p.get_proximo() != None):
            print(p.get_dado().get_filmeeano())
            p = p.get_proximo()

mov0 = Dadu('filme0', 2000)
no0 = mov0
mov2 = Dadu('filme2', 2005)
no1 = mov2
mov1 = Dadu('filme1', 2001)
no2 = mov1
lista =Lista()
lista.ordenar()
lista.printar_all()
