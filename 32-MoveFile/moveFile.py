import os

source = "C:\\Users\\yashar.tukhfatullin\\Desktop\\Computer Science Tutorial\\test.txt"
destination = "C:\\Users\\yashar.tukhfatullin\\Desktop\\Computer Science Tutorial\\Python-Fundamentals-2024\\32-MoveFile\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
except FileNotFoundError:
    print(f"{source} was not found  ")
