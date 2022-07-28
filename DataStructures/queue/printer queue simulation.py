from queue import *
from random import randint
from time import *
from threading import *

class Person:
    # ansi
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
                           f"| {round(self.total_time, 1)}" + self.END)

    def finish(self):
        print(self.BLUE + f"person {self.id} finished" + self.END)


def enqueue():
    global x, total
    while True:
        p = Person(x)
        total += p.print_time
        p.total_time += total
        p.status()
        q.push(p)
        x += 1
        sleep(0.5)


def dequeue():
    global total
    while True:
        if not q.is_empty():
            p = q.peek()
            p.finish()
            sleep(p.print_time)
            q.pop()
            total -= p.print_time
            sleep(0.5)






q = Queue()
x = 1
total = 0

t1 = Thread(target=enqueue)
t2 = Thread(target=dequeue)

t1.start()
t2.start()

t1.join()
t2.join()








