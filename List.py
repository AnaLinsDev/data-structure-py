from Node import Node
from Data import Data

class List:
    def __init__(self, head=None):  # Construtor
        self._head = head
        self._size = 0

    def show(self, index):  # Mostra de acordo com o index
        p = self._head
        if p == None:
            print('Empty')
        elif index > self.length() - 1:
            print(' Invalid ID ')
        elif index < self.length():
            for i in range(index):
                if p.get_next() != None:
                    p = p.get_next()
            print(p.get_data().get_movieeyear())

    def showyear(self, index):  # Mostra de acordo com o index
        p = self._head
        a = self
        for i in range(index):
            if p.get_next() != None:
                p = p.get_next()
        return p.get_data().get_year()

    def isEmpty(self):  # Vazia
        if self.length() == 0:
            return True
        else:
            return False

    def insert(self, index, elem):  # Inserir
        if self._head == None and index == 0 :
            node = Node(elem)
            node.set_next(None)
            self._head = node
        if index > self.length():
            print(' Invalid ID ')
        elif index == 0 :
            node = Node(elem)
            node.set_next(self._head)
            self._head = node
        else:
            node = Node(elem)
            q = self._head
            for i in range(index - 1):
                if q.get_next() != None:
                    q = q.get_next()
            node.set_next(q.get_next())
            q.set_next(node)

    def remove(self, index):  # Remover um item node indice
        p = self._head
        if self.length() == 0:
            print('Empty')
        elif index == 0:
            p = self._head
            if p != None:
                self._head = self._head.get_next()
        elif index >= self.length():
            print(' Invalid ID ')
        elif p != None:
            q = self._head.get_next()
            for i in range(index - 1):
                q = q.get_next()
                p = p.get_next()
            if q != None:
                p.set_next(q.get_next())
                q.set_next(p)

    def sort(self):
        if self.length() == 0:
            print('Empty')
        else:
            ordem = False
            while not ordem:
                ordem = True
                p = self._head
                q = p.get_next()
                while q.get_next() != None:
                    if p.get_data().get_year() > q.get_data().get_year():
                        ordem = False
                        aux = p.get_data()
                        p.set_data(q.get_data())
                        q.set_data(aux)
                    p = q
                    q = q.get_next()

    def length(self):
        p = self._head
        count = 0
        if p != None:
            while p.get_next() != None:
                p = p.get_next()
                count += 1
        return count

    def print_all(self):
        p = self._head
        i = 0
        if p != None:
            while (p.get_next() != None):
                print(f' id{i} -> {p.get_data().get_movieeyear()}')
                i += 1
                p = p.get_next()
        else:
            print('Empty')

    def menu(self):
        print( """List
        \n 0 - Finished
        \n 1 - Add using id
        \n 2 - Remove using id
        \n 3 - It's Empty  
        \n 4 - Show Size 
        \n 5 - Show All 
        \n 6 - Show by id
        \n 7 - Sort List
        """)


lis = List()
lis.menu()
r = input(" Type your choice: ")
while (r != '0'):
    if r == "1":
        movie = input("MOVIE: ")
        year = int(input("YEAR: "))
        index = int(input("ID: "))
        lis.insert(index, Data(movie, year))
        print("...")
        lis.menu()
        r = input(" Type your choice: ")
    elif r == "2":
        print("...")
        i = int(input("Which ID would you like to remove?  "))
        lis.remove(i)
        print("...")
        lis.menu()
        r = input(" Type your choice: ")
    elif r == "3":
        print(lis.isEmpty())
        lis.menu()
        r = input(" Type your choice: ")
    elif r == "4":
        print("O tamanho da lista é: ", lis.length())
        lis.menu()
        r = input(" Type your choice: ")
    elif r == "5":
        lis.print_all()
        lis.menu()
        r = input(" Type your choice: ")
    elif r == "6":
        i = int(input("Which ID would you like to search?  "))
        lis.show(i)
        lis.menu()
        r = input(" Type your choice: ")
    elif r == "7":
        lis.sort()
        print("...")
        lis.menu()
        r = input(" Type your choice: ")
    else:
        print('Invalid, Try again')
        lis.menu()
        r = input(" Type your choice: ")
