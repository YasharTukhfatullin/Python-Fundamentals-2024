"""
function = a block of code which is executed only when it is called.

arguments are the information sending to a function 
you need a matching set of parameters
"""


def hello():
    print("Hello world")


hello()
print("==========")


def say_hello(name):
    print("Hi " + name)


say_hello("Yashar")
print("==========")


def say_new_hello(first_name, last_name):
    print("Hi " + first_name + last_name)


say_new_hello("Yashar", " Tukhfatullin")
print("==========")

print("==========")


def say_new_hello_age(first_name, last_name, age):
    print("Hi " + first_name + last_name)
    print("You are " + str(age) + " years old")


say_new_hello_age("Yashar", " Tukhfatullin", 21)
print("==========")
