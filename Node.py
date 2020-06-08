from Data import Data 

class Node:
    def __init__(self, data = Data(), next = None):
        self._data = data
        self._next = next
    def get_data(self):
        return self._data
    def set_data(self, newdata):
        self._data = newdata
    def get_next(self):
        return self._next
    def set_next(self, n):
        self._next = n
    def size(self):
        return len(self._data)
    def __str__(self):
        return "{}".format(self._data)


