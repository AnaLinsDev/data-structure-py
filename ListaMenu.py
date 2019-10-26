

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
        if self.length() == 0:
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
            p = self._head
            if p != None:
                self._head = self._head.get_proximo()
            else: 
                print(' A lista ja está vazia !')
        else:
            p = self._head
            if index > self.length():
                print ( ' indice invalido ')
            elif p != None:
                q = self._head.get_proximo()
                for i in range(index - 1):
                    q = q.get_proximo()
                    p = p.get_proximo()
                if q != None:
                    p.set_proximo(q.get_proximo())
                    q.set_proximo(p)
            else:
                print(' A lista ja está vazia !')
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
        if p != None:
            while p.get_proximo() != None :
                p =p.get_proximo()
                count+=1
        return count
    def printar_all(self):
        p = self._head
        i = 0
        while(p.get_proximo() != None):
            print(f' pos: {i} -> {p.get_dado().get_filmeeano()}')
            i +=1
            p = p.get_proximo()

print("IFPB - Instituto Federal da Paraiba ")
print("-=-"*20)
lis = Lista()
r = input(""" 
_________________________________
|  ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█    |
|  ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█    |
|  ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀    |   
|_______________________________|
| 0) sair do Menu               |
| 1) adicionar                  |
| 2) remover                    |
| 3) Mostrar se está vazia      |
| 4) Mostrar tamanho da Lista   |
| 5) Mostrar tudo               |
| 6) Mostrar por indice         |
| 7) Deixar a lista ordenada    |
|_______________________________|

🔴 Digite sua opção: 
""")
while (r != '0') :
    if r == "1":
        a = input("Qual FILME você quer adicionar: ")

        b = int(input("Qual ANO você quer adicionar: "))
        i = int(input("Qual a posição que deseja adicionar ?")) 
        lis.insert(i, Dadu(a,b))
        print("...")
        time.sleep(1)
        r = input(""" 
_________________________________
|  ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█    |
|  ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█    |
|  ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀    |   
|_______________________________|
| 0) sair do Menu               |
| 1) adicionar                  |
| 2) remover                    |
| 3) Mostrar se está vazia      |
| 4) Mostrar tamanho da Lista   |
| 5) Mostrar tudo               |
| 6) Mostrar por indice         |
| 7) Deixar a lista ordenada    |
|_______________________________|

🔴 Digite sua opção: 
""")
    elif r == "2":
        print("...")
        time.sleep(1)
        i = int(input("De qual indice deseja remover?"))
        lis.remove(i)
        print("...")
        time.sleep(1)
        print("O elemento da fila foi removido!")
        r = input(""" 
_________________________________
|  ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█    |
|  ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█    |
|  ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀    |   
|_______________________________|
| 0) sair do Menu               |
| 1) adicionar                  |
| 2) remover                    |
| 3) Mostrar se está vazia      |
| 4) Mostrar tamanho da Lista   |
| 5) Mostrar tudo               |
| 6) Mostrar por indice         |
| 7) Deixar a lista ordenada    |
|_______________________________|

🔴 Digite sua opção: 
""")
    elif r =="3":
        print(lis.isEmpty())
        r = input(""" 
_________________________________
|  ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█    |
|  ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█    |
|  ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀    |   
|_______________________________|
| 0) sair do Menu               |
| 1) adicionar                  |
| 2) remover                    |
| 3) Mostrar se está vazia      |
| 4) Mostrar tamanho da Lista   |
| 5) Mostrar tudo               |
| 6) Mostrar por indice         |
| 7) Deixar a lista ordenada    |
|_______________________________|

🔴 Digite sua opção: 
""")
    elif r == "4":
        print("O tamanho da lista é: ",lis.length())
        r = input(""" 
_________________________________
|  ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█    |
|  ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█    |
|  ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀    |   
|_______________________________|
| 0) sair do Menu               |
| 1) adicionar                  |
| 2) remover                    |
| 3) Mostrar se está vazia      |
| 4) Mostrar tamanho da Lista   |
| 5) Mostrar tudo               |
| 6) Mostrar por indice         |
| 7) Deixar a lista ordenada    |
|_______________________________|

🔴 Digite sua opção: 
""")
    elif r == "5":
        lis.printar_all()
        r = input(""" 
_________________________________
|  ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█    |
|  ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█    |
|  ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀    |   
|_______________________________|
| 0) sair do Menu               |
| 1) adicionar                  |
| 2) remover                    |
| 3) Mostrar se está vazia      |
| 4) Mostrar tamanho da Lista   |
| 5) Mostrar tudo               |
| 6) Mostrar por indice         |
| 7) Deixar a lista ordenada    |
|_______________________________|

🔴 Digite sua opção: 
""")
    elif r == "6":
        i = int(input('Qual indice do elemento que deseja ver ?'))
        lis.mostrar(i)
        r = input(""" 
_________________________________
|  ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█    |
|  ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█    |
|  ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀    |   
|_______________________________|
| 0) sair do Menu               |
| 1) adicionar                  |
| 2) remover                    |
| 3) Mostrar se está vazia      |
| 4) Mostrar tamanho da Lista   |
| 5) Mostrar tudo               |
| 6) Mostrar por indice         |
| 7) Deixar a lista ordenada    |
|_______________________________|

🔴 Digite sua opção: 
""")
    elif r == "7":
        lis.ordenar()
        print("...")
        time.sleep(1)
        print('A lista foi ordenada com sucesso !')
        r = input(""" 
_________________________________
|  ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█    |
|  ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█    |
|  ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀    |   
|_______________________________|
| 0) sair do Menu               |
| 1) adicionar                  |
| 2) remover                    |
| 3) Mostrar se está vazia      |
| 4) Mostrar tamanho da Lista   |
| 5) Mostrar tudo               |
| 6) Mostrar por indice         |
| 7) Deixar a lista ordenada    |
|_______________________________|

🔴 Digite sua opção: 
""")
    else:
        print('Opção invalida')
        r = input(""" 
_________________________________
|  ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█    |
|  ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█    |
|  ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀    |   
|_______________________________|
| 0) sair do Menu               |
| 1) adicionar                  |
| 2) remover                    |
| 3) Mostrar se está vazia      |
| 4) Mostrar tamanho da Lista   |
| 5) Mostrar tudo               |
| 6) Mostrar por indice         |
| 7) Deixar a lista ordenada    |
|_______________________________|

🔴 Digite sua opção: 
""")
