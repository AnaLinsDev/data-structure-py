from Node import Node
from Data import Data

class Stack :
    def __init__ ( self, topo = None):
        self._topo = topo
    def isEmpty(self):
        p = self._topo
        if p == None:
            return True
        else:
            return False
    def add(self, elem):
        elem.set_next(self._topo)
        self._topo = elem
    def remove(self):
        p = self._topo
        if p == None:
            print(' Stack is empty ')
        elif self.sizep() != 1:
            self._topo = self._topo.get_next()
        else:
            self._topo = None
    def sizep(self):
        p = self._topo
        count = 0
        if p != None:
             while p != None:
              count+=1
              p = p.get_next()
        return count

    def showtop(self):
        p = self._topo
        if p != None:
            return self._topo.get_data().get_movieeyear()
        else:
            return 'Empty'
    def menu(self):
        print( """Stack 
        \n 0 - Finished
        \n 1 - Add
        \n 2 - Remove 
        \n 3 - It's Empty  
        \n 4 - Show Size 
        \n 5 - Show Top 
        """)

stack = Stack()
stack.menu()
r = input(" Type your choice: ")
while (r != "0") :
    if r == "1":
        movie = input("Which MOVIE would you like to add? ")
        year = int(input("Which YEAR would you like to add: "))
        stack.add(Node(Data(movie,year)))
        print("...")
        stack.menu()
        r = input(" Type your choice: ")
    elif r == "2":
        print("...")
        stack.remove()
        stack.menu()
        r = input(" Type your choice: ")
    elif r =="3":
        print(stack.isEmpty())
        stack.menu()
        r = input(" Type your choice: ")
    elif r == "4":
        print("Size: ",stack.sizep())
        stack.menu()
        r = input(" Type your choice: ")
    elif r == "5":
        print("Top : ",stack.showtop())
        stack.menu()
        r = input(" Type your choice: ")
    else:
        print('Invalid, Try again')
        stack.menu()
        r = input(" Type your choice: ")
