from threading import Thread
import time


def sleeper(n, name):
    print("Hi i am {} going to sleep for 5 sec".format(name))
    time.sleep(n)

    print("{} i woken up from sleep".format(name))


t1 = Thread(target=sleeper, name="thread1", args=(5, 'thread1'))
t1.start()