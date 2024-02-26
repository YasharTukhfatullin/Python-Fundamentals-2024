"""
copyfile() = copies contents of a file
copy() = copyfile() + permission mode + destination can be a directory
copy2() = copy() + copies metadata (file's creation and modification times)
"""
import shutil 

shutil.copyfile("C:\\Users\\yashar.tukhfatullin\\Desktop\\Computer Science Tutorial\\Python-Fundamentals-2024\\31-CopyFile\\test.txt", "C:\\Users\\yashar.tukhfatullin\\Desktop\\Computer Science Tutorial\\Python-Fundamentals-2024\\31-CopyFile\\copy.txt") #src, dst