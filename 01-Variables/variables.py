'''
Variable = a container for a value. Behaves as the value that it contains.
'''
# str = string a series of characters
first_name = "Yashar"
last_name = "Tukhfatullin"
full_name = first_name + last_name
print(first_name)
print(last_name)
print("Hello " + first_name)
print(type(first_name))
print(full_name)
print("======================")

# int = integer a whole number
age = 25
age = age + 1
age += 1
print(age)
print(type(age))
print("Your age is: " + str(age))
print("======================")

# float = floating point number a decimal number
height = 250.5
print(height)
print(type(height))
print("Your height is: " + str(height) + "cm")
print("======================")

# boolean = true or false
human = True
print(human)
print(type(human))
print("Are you a human: " + str(human))
print("======================")

'''
Multiple assignment = allows us to assign multiple variable at the same time in one line of code.
'''

new_name, new_age,new_attractive = "Ryan", 21, True
print(new_name)
print(new_age)
print(new_attractive)
print("======================")

Ryan = Jake = Josh = Kyle = 30
print(Ryan)
print(Jake)
print(Josh)
print(Kyle)

