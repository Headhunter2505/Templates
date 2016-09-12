import multiprocessing
import time


# doesn't work yet


def command1():
    time.sleep(10)
    print("1")


def command2():
    time.sleep(5)
    print("2")


p1 = multiprocessing.Process(target=command1())
p2 = multiprocessing.Process(target=command2())

p1.start()
p2.start()
