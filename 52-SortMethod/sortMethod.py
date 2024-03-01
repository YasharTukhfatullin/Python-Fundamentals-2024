"""
sort() method = used with lists
sort() function = used with iterables
"""

students = ["Ryan", "Bryson", "Jake", "Andrew", "Yashar"]
students.sort()
for i in students:
    print(i)
print("==================")

sorted_students = sorted(students, reverse=True)
for i in sorted_students:
    print(i)
print("==================")

new_students_a = [
    ("Ryan", "F", 60),
    ("Jake", "A", 33),
    ("Bryson", "D", 36),
    ("Andrew", "B", 20),
    ("Josh", "C", 78),
]

new_students_a.sort()
for i in new_students_a:
    print(i)
print("==================")

new_students_b = [
    ("Ryan", "F", 60),
    ("Jake", "A", 33),
    ("Bryson", "D", 36),
    ("Andrew", "B", 20),
    ("Josh", "C", 78),
]

grade = lambda grades: grades[1]
new_students_b.sort(key=grade)
for i in new_students_b:
    print(i)
print("==================")

new_students_c = [
    ("Ryan", "F", 60),
    ("Jake", "A", 33),
    ("Bryson", "D", 36),
    ("Andrew", "B", 20),
    ("Josh", "C", 78),
]

age = lambda ages: ages[2]
new_students_c.sort(key=age)
for i in new_students_c:
    print(i)
print("==================")

new_students_tuple = (
    ("Ryan", "F", 60),
    ("Jake", "A", 33),
    ("Bryson", "D", 36),
    ("Andrew", "B", 20),
    ("Josh", "C", 78),
)

age = lambda ages: ages[2]
sorted_students_tuple = sorted(new_students_tuple, key=age)
for i in sorted_students_tuple:
    print(i)
print("==================")
