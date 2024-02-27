class Car:

    wheels = 4  # class variable

    # initialize(constructor) method will construct object for us
    def __init__(self, make, model, year, color):
        self.make = make  # attributes describe what an object is. self is referring to the object we currently working on
        self.model = model
        self.year = year
        self.color = color
