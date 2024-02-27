"""
Object Oriented Programming OOP = An object is instance of a class
we can create representation of real-life object.

Attributes = is/she example: name, age, height 
Methods = actions example: eat, sleep, make YouTube videos.

Class can function as a blueprint to create objects.
We can assign attributes what describe an object is or has.
Methods what each object can do.
Within a our class we have a special method __init__ pass some arguments to each 
"""

from car import Car

# car_1 is an object
car_1 = Car("Chevy", "Corvet", 2021, "Blue")  # passing an argument
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()
print("============================================")

car_2 = Car("Ford", "Focus", 2024, "Red")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()
