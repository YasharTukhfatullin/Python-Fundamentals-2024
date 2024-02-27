class Car:
    # initialize method will construct object for us
    def __init__(self, make, model, year, color):
        self.make = make  # attributes describe what an object is. self is referring to the object we currently working on
        self.model = model
        self.year = year
        self.color = color

    def drive(self):  # self refers to the object that is using this method
        print(f"This {self.model} is driving")

    def stop(self):
        print(f"This {self.model} is stopped")
