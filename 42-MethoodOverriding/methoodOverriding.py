"""Method overriding is ability of an OOP to allow a subclass(child) 
to provide a specific implementation of a method that is provided by one of its 
parents in this case we will override the eat method and provide more 
specific implementation for rabbit class"""


class Animal:
    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):
    def eat(self):  # overriding a method with self
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()
