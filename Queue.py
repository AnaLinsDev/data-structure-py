from Node import Node
from Data import Data

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
        elem.set_next(self._head)
        self._head = elem
        return elem.get_data()
    def remove(self):
        p = self._head
        if self.sizef() == 1 :
            self._head = None
            print('Empty')
        elif p == None:
            print('Empty')
        elif p.get_next() != None:
            while p.get_next().get_next() != None: #penultimo
              p = p.get_next()
            p.set_next(None)

    def sizef(self):
        p = self._head
        count = 0
        if p != None:
            while p != None:
                count+=1
                p =p.get_next()
        return count
    def showhead(self):
        p = self._head
        if p == None:
            return 'Empty'
        elif p != None:
            if p.get_data() != None:
                while p.get_next() != None:
                    p = p.get_next()
                return p.get_data().get_movieeyear()
    def menu(self):
        print( """Queue
        \n 0 - Finished
        \n 1 - Add
        \n 2 - Remove 
        \n 3 - It's Empty  
        \n 4 - Show Size 
        \n 5 - Show Top 
        """)
fil = Fila()
fil.menu()
r = input(" Type your choice: ")

while (r != '0') :
    if r == "1":
        movie = input("Which MOVIE would you like to add? ")
        year = int(input("Which YEAR would you like to add: "))
        fil.add(Node(Data(movie,year)))
        print("...")
        fil.menu()
        r = input(" Type your choice: ")

    elif r == "2":
        print("...")
        fil.remove()
        fil.menu()
        r = input(" Type your choice: ")

    elif r =="3":
        print(fil.isEmpty())
        fil.menu()
        r = input(" Type your choice: ")

    elif r == "4":
        print("Size: ",fil.sizef())
        fil.menu()
        r = input(" Type your choice: ")

    elif r == "5":
        print("Top : ",fil.showhead())
        fil.menu()
        r = input(" Type your choice: ")
    else:
        print('Invalid, Try again')
        fil.menu()
        r = input(" Type your choice: ")
