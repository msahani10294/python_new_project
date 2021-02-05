from threading import Thread, Lock


x = 0
COUNT = 100000


def adding_2():

    global x

    for i in range(COUNT):
        x += 2


def adding_3():

    global x

    for i in range(COUNT):
        x += 3


def subtract_4():
    global x

    for i in range(COUNT):
        x -= 4


def subtract_1():
    global x

    for i in range(COUNT):
        x -= 1





