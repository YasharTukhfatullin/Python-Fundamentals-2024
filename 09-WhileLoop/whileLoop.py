"""
while loop = a statement that will execute it's block of code,
            as long as it's condition remains true.
"""

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)
print("===============")


new_name = None  # instead of null python uses None

while not new_name:
    new_name = input("Enter your new name?")

print("Hi " + new_name)
