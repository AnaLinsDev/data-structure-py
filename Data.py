class Data:
    def __init__(self, movie=None, year=None):
        self._movie = movie   
        self._year = year
    def get_movie(self):
        return self._movie
    def get_year(self):
        return self._year
    def set_movie(self, new):
         self._movie = new
    def set_year(self, new):
        self._year = new
    def set_movieeyear(self,newmovie, newyear):
        self._movie = newmovie
        self._year = newyear
    def get_movieeyear(self):
        return f'm:{self._movie} -> y:{self._year}'
    





