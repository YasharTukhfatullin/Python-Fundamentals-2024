""" list comprehension = a way to create a new list with less syntax
can mimic certain lambda functions, easier to read.

list = [expression for item in iterable]
list = [expression for item in iterable if condition]
list = [expression if/else for item in iterable] 
"""

# Creating a normal list numbers
squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)
print("=============")

# Using list comprehension
new_squares = [i * i for i in range(1, 11)]
print(new_squares)
print("=============")

# Creating normal lambda
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)
print("=============")

# Using list comprehension lambda
new_students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
new_passed_students = [i for i in new_students if i >= 60]
print(passed_students)
print("=============")

new_students_fail = [100, 90, 80, 70, 60, 50, 40, 30, 0]
new_passed_students_fail = [i if i >= 60 else "Fail" for i in new_students_fail]
print(new_passed_students_fail)
print("=============")
