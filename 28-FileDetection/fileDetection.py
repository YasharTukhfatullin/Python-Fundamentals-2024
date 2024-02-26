import os

path = "C:\\Users\\yashar.tukhfatullin\\Desktop\\Computer Science Tutorial\\Python-Fundamentals-2024\\28-FileDetection\\variables.txt"

if os.path.exists(path):
    print("This location is exists")
    if os.path.isfile(path):
        print("This is a file variable")
    elif os.path.isdir(path):  # checking if folder is exits
        print("That is directory (folder)")
else:
    print("This location doesn't exists")
