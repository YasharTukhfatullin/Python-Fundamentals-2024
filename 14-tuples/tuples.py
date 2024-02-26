"""
tuples = collection which is order and unchangeable
          used to group together related data.
"""

student = ("Kyle", 21, "male")
print(student)

print(student.count("Kyle"))
print(student.index("male"))
print("===============")

for x in student:
    print(x)
print("===============")

if "Kyle" in student:
    print("Kyle is here")
