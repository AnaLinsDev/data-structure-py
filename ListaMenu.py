# ta td dando errado, to tentando consertar k
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
        print(p.get_dado().get_filmeeano())
    def isEmpty(self): #Vazia
        if self._head == None:
            print(True)
        else: print(False)
    def insert(self, index, elem): #Inserir
            no = elem 
            if self._head == None:
                no.set_proximo(None)
                self._head = no
            if index > self.length():
                print ( ' indice invalido ')
            else:
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

print("IFPB - Instituto Federal da Paraiba ")
print("-=-"*20)
lis = Lista()
r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Lista
5) Mostrar tudo
6) Mostrar por indice
7) Deixar a lista ordenada
Digite sua opção: 
""")
while (r != '0') :
    if r == "1":
        a = input("Qual FILME você quer adicionar: ")
        b = input("Qual ANO você quer adicionar: ")
        i = int(input("Qual a posição que deseja adicionar ?")) 
        lis.insert(i, No(Dadu(a,b)))
        print("...")
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Lista
5) Mostrar tudo
6) Mostrar por indice
7) Deixar a lista ordenada
Digite sua opção:
""")
    elif r == "2":
        print("...")
        time.sleep(1)
        i = int(input("De qual indice deseja remover?"))
        lis.remove(i)
        print("O elemento da fila foi removido!")
        r = input("""
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Lista
5) Mostrar tudo
6) Mostrar por indice
7) Deixar a lista ordenada
Digite sua opção:     
""")
    elif r =="3":
        lis.isEmpty()
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Lista
5) Mostrar tudo
6) Mostrar por indice
7) Deixar a lista ordenada
Digite sua opção: """)
    elif r == "4":
        print("O tamanho da lista é: ",lis.length())
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Lista
5) Mostrar tudo
6) Mostrar por indice
7) Deixar a lista ordenada
Digite sua opção:""")
    elif r == "5":
        lis.printar_all()
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Lista
5) Mostrar tudo
6) Mostrar por indice
7) Deixar a lista ordenada
Digite sua opção:""")
    elif r == "6":
        i = int(input('Qual indice do elemento que deseja ver ?'))
        lis.mostrar(i)
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Lista
5) Mostrar tudo
6) Mostrar por indice
7) Deixar a lista ordenada
Digite sua opção:""")
    elif r == "7":
        lis.ordenar()
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Lista
5) Mostrar tudo
6) Mostrar por indice
7) Deixar a lista ordenada
Digite sua opção:""")





