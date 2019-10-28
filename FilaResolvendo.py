from Node import No
from Cdados import Dadu
import time

class Fila: 
    def __init__ ( self, head = None):
        self._head = head
    def isEmpty(self):
        p = self._head
        if p == None:
            return True
        else: 
            return False
    def add(self, elem):
        elem.set_proximo(self._head)
        self._head = elem
        return elem.get_dado()
    def remove(self):
        p = self._head
        if self.sizef() == 1 :
            self._head = None
            p = None
            print('Lista vazia')
        elif p == None:
            print(' Lista Vazia ') 
        elif p.get_proximo() != None:
            while p.get_proximo().get_proximo() != None: #penultimo 
              p = p.get_proximo()
            p.set_proximo(None)

    def sizef(self):
        p = self._head
        count = 0 
        if p == None:
            return count
        if p != None:
            while p != None:
                count+=1
                p =p.get_proximo()
            return count
    def showhead(self):
        p = self._head
        if p == None:
            return 'Vazio'
        elif p != None:
            if p.get_dado() != None:
                while p.get_proximo() != None:
                    p = p.get_proximo()
                return p.get_dado().get_filmeeano()
            else: 
                return 'Vazio'
fil = Fila()
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
| 4) Mostrar tamanho da Fila   |
| 5) Mostrar head               |
|_______________________________|

🔴 Digite sua opção: 
""")

while (r != '0') :
    if r == "1":
        a = input("Qual FILME você quer adicionar: ")
        b = int(input("Qual ANO você quer adicionar: "))
        fil.add(No(Dadu(a,b)))
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
| 4) Mostrar tamanho da Fila   |
| 5) Mostrar head               |
|_______________________________|

🔴 Digite sua opção: 
""")

    elif r == "2":
        print("...")
        time.sleep(1)
        fil.remove()
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
| 4) Mostrar tamanho da Fila   |
| 5) Mostrar head               |
|_______________________________|

🔴 Digite sua opção: 
""")

    elif r =="3":
        print(fil.isEmpty())
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
| 4) Mostrar tamanho da Fila   |
| 5) Mostrar head               |
|_______________________________|

🔴 Digite sua opção: 
""")

    elif r == "4":
        print("O tamanho da fila é: ",fil.sizef())
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
| 4) Mostrar tamanho da Fila   |
| 5) Mostrar head               |
|_______________________________|

🔴 Digite sua opção: 
""")

    elif r == "5":
        print("O head é : ",fil.showhead())
        time.sleep((1))
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
| 4) Mostrar tamanho da Fila   |
| 5) Mostrar head               |
|_______________________________|

🔴 Digite sua opção: 
""")
    else:
        print('Opção invalida')
        time.sleep((1))
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
| 4) Mostrar tamanho da Fila   |
| 5) Mostrar head               |
|_______________________________|

🔴 Digite sua opção: 
""")
