  
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
        return print(p.get_dado().get_dado().get_filmeeano())
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
        while(p != None):
            print(p.get_dado().get_dado().get_filmeeano())
            p = p.get_proximo()
    def show(self, index):
        p = self._head
        for i in range(index):
            p = p.get_proximo()
        return p.get_dado().get_dado().get_filmeeano()
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
    def length(self):
        p =self._head
        count = 0
        while p.get_proximo() != None:
            p =p.get_proximo()
            count+=1
        return count
print("IFPB - Instituto Federal da Paraiba ")
print("-=-"*20)
lis = Lista()
r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar tudo
6) Mostrar por indice
Digite sua opção: 
""")
while (r != '0') :
    if r == "1":
        a = input("Qual FILME você quer adicionar: ")
        b = input("Qual ANO você quer adicionar: ")
        i = int(input("Qual a posição que deseja adicionar ?")) 
        lis.insert(i, No(Dadu(a,b)))
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("O elemento foi adicionado com sucesso!")
        time.sleep(1)
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar tudo
6) Mostrar por indice
Digite sua opção:
""")
    elif r == "2":
        print("...")
        time.sleep(1)
        i = input("De qual indice deseja remover?")
        lis.remove(i)
        print("O elemento da fila foi removido!")
        time.sleep(1)
        r = input("""
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar tudo
6) Mostrar por indice
Digite sua opção:     
""")
    elif r =="3":
        lis.isEmpty()
        time.sleep(1)
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar tudo
6) Mostrar por indice
Digite sua opção: """)
    elif r == "4":
        print("O tamanho da pilha é: ",lis.length())
        time.sleep(1)
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar tudo
6) Mostrar por indice
Digite sua opção:""")
    elif r == "5":
        print(lis.printar_all())
        time.sleep(1)
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar tudo
6) Mostrar por indice
Digite sua opção:""")
    elif r == "6":
        i = int(input('Qual indice do elemento que deseja ver ?'))
        print(f'no indice {i}, o elemento é {lis.show(i)}')
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar tudo
6) Mostrar por indice
Digite sua opção:""")



