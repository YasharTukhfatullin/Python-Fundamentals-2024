"""
for loop = a statement that will execute it's block of code a limited amount of times.

while loop = unlimited times

for loop = limited times
"""

import time

for i in range(10):
    print(i)
print("===========")

for i in range(50, 100):
    print(i)
print("===========")

for i in "Yashar Tukhfatullin":
    print(i)
print("===========")

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year")
