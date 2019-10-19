from Node import No
from Cdados import Dadu
import time

class Pilha:
    def __init__ ( self, topo = No()):
        self._topo = topo
    def isEmpty(self):
        if self._topo.get_dado() == None:
            print("True")
        else:
            print("False")
    def add(self, elem):
        elem.set_proximo(self._topo)
        self._topo = elem
    def remove(self):
        self._topo = self._topo.get_proximo()
    def sizep(self):
        p = self._topo
        count = 0
        while p.get_proximo() != None:
            count+=1
            p = p.get_proximo()
        return count
    def showtopo(self):
        print(self._topo.get_dado())
    def printar_all(self):
        p = self._topo
        while(p != None):
            print(p.get_dado().get_filmeeano())
            p = p.get_proximo()

pil = Pilha()
r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Pilha
5) Mostrar o topo
Digite sua opção: 
""")
if r == '0' :
    print('não há nenhum filme adicionado')
    

while r != '0':
    if r == "1":
        a = input("Qual filme você quer adicionar : ")
        b =input("Qual  ano  você quer adicionar : ")
        pil.add(No(Dadu(a, b)))
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
    4) Mostrar tamanho da Pilha
    5) Mostrar o topo
    Digite sua opção:
    """)
  
    elif r == "2":
        print("...")
        time.sleep(1)
        print("O elemento da fila foi removido!")
        time.sleep(1)
        r = input("""
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Pilha
5) Mostrar o topo
Digite sua opção:     
""")
    elif r =="3":
        pil.isEmpty()
        time.sleep(1)
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Pilha
5) Mostrar o topo
Digite sua opção: """)
    elif r == "4":
        print("O tamanho da pilha é: ",pil.sizep())
        time.sleep(1)
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Pilha
5) Mostrar o topo
Digite sua opção:""")
    elif r == "5":
        print("O tamanho do topo é: ",pil.showtopo())
        time.sleep((1))
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Pilha
5) Mostrar o topo
Digite sua opção: """)
pil.printar_all()


