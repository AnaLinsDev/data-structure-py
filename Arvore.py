class NoAr:
    def __init__(self, dado=None, left=None, right=None, father=None):
        self._dado = dado
        self._left = left
        self._right = right
        self._father = father
    def get_left(self):
        return self._left
    def get_right(self):
        return self._right
    def get_dado(self):
        return self._dado
    def get_father(self):
        return self._father
    def set_left(self, no):
        if self.get_left == None:
            print( 'O No esquerdo ja existe')
        else: self._left = no
    def set_right(self, no):
        if self.get_right == None:
            print( 'O No direito ja existe')
        else: self._right = no
    def set_dado(self, new):
        self._dado = new
    def set_father(self, new):
        self._father = new


tree = NoAr()

tree.set_dado(7)
tree.set_left(3)
tree.set_right(5)

print(tree._dado)
print(tree._left)
print(tree._right)


    
