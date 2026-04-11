from building import *
from data_structures import Stack

class History:
    def __init__(self):
        self.nav = Stack()
    def add(self,start : Building, end : Building, along : list, total : int):
        #starting point, end  point, buildings passed on the way in order, total time spent
        self.nav.push([start,end,along,total])
    def remove(self):
        return self.nav.pop()
