import os

path = "C:\\Users\\yashar.tukhfatullin\\Desktop\\Computer Science Tutorial\\Python-Fundamentals-2024\\33-DeleteFile\\test.txt"

try:
    # os.remove(path)     delete a file
    # os.rmdir(path)      delete an empty directory
    # shutil.rmtree(path) delete a directory containing files
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You got not have permission to delete that")
except OSError:
    print("You dont not have permission to delete that")
else:
    print(f"{path} was deleted ")
