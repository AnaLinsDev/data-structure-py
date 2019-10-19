from Node import No
from Cdados import Dadu 

class Lista:
    def __init__(self, head = None, lis=[]):
        self._head = head
        self._size = 0

    def mostrar(self, index):
        p = self._head
        for i in range(index):
            if p.get_proximo() != None:
                p = p.get_proximo()
        return print(p)
    def isEmpty(self): #Vazia
        if self._head == None:
            return True
        else: return False
    def size(self): #Tamanho
        p = self._head
        count = 0
        while p.get_proximo() != None:
            count = count + 1
            p = p.get_proximo()
        return count
    def insert(self, index, elem): #Inserir
            if index == 0:
                no = No(elem)   #aqui esta tipo : No(No('filme0', 2000))
                no.set_proximo(self._head)
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

    def length(self):
        p = self._head
        count = 0
        while (p!= None):
            count += 1
            p = p.get_proximo()
        return count
    def printar_all(self):
        p = self._head
        while(p != None):
            print(p)
            p = p.get_proximo()
    def show(self, index):
        p = self._head
        for i in range(index):
            p = p.get_proximo()
        return p
    def ordenar(self,param):
        if (param == "+"):     #Crescente
            lis =[]
            p = self._head
            i = 0
            while p!= None:
                if (self.show(i).get_dado().get_ano() not in lis):
                    lis.append(self.show(i).get_dado().get_ano())
                p = p.get_proximo()
                i += 1
            lis.sort()
            print(lis)
        elif (param == "-"):    #Decrescente
            lis = []
            p = self._head
            i = 0
            while p.get_proximo() != None:
                if (self.show(i).get_dado().get_ano() not in lis):
                    lis.append(self.show(i).get_dado().get_ano())
                p = p.get_proximo()
                i += 1
            lis.sort(reverse=True)
            print(lis)
        else:
            print("Parâmetro inválido!")

mov0 = Dadu('filme0', 2000)
no0 = mov0 
mov2 = Dadu('filme2', 2002)
no1 = mov2 
mov1 = Dadu('filme1', 2001)
no2 = mov1 

lista =Lista()
lista.insert(0, no0)
lista.insert(0, no1)
lista.insert(0, no2)
print(lista.length())
lista.ordenar()















'''
lista = Lista()
lista.insert(0, No(0))
lista.insert(1, No(1))
lista.insert(4, No(2))
lista.remove(5)
lista.remove(1)
lista.printar_all()
print(f'tamanho: {lista.lenght()}')
'''
