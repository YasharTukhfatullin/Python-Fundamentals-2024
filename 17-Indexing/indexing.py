"""
index operator [] = gives access to a sequence's element (str, list, tuples)
"""

name = "Yashar Tukhfatullin"

if (name[0] == name.islower()):
  name = name.capitalize()
print(name)
print("==========")

first_name = name[0:3].upper()
print(first_name)

last_name = name[7:].lower()
print(last_name)

last_character = name[-1]
print(last_character)