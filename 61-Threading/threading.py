"""
Thread = a flow of execution. Like a separate order of instructions.
However each thread takes a turn running to achieve concurrency
GIL = (global interpreter lock), allows only one thread to hold the control of the Python interpreter at any one time

cpu bound = program/task spends most of it's time waiting for internal events (CPU into use multiprocessing)

io bound = program/task spends most of it's time waiting for external events (user inputs use multithreading)

CPU Bound = program/task spends most of 
"""

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")


def drinking_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish study")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drinking_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# eat_breakfast()
# drinking_coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
