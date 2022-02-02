from queue import *
from random import randint


class Person:

    BLUE = "\033[0;34m"
    GREEN = "\033[0;32m"
    END = "\033[0m"

    def __init__(self, ID):
        self.id = ID
        self.pages = randint(1, 25)
        self.print_time = self.pages / 10
        self.total_time = 0

    def status(self):
        print(self.GREEN + f"person {self.id} | pages -> {self.pages} | print time -> {self.print_time} "
              f"| {self.total_time}" + self.END)

    def finish(self):
        print(self.BLUE + f"person {self.id} finished" + self.END)





































