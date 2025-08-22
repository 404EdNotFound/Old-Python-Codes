class Car: #Class is being defined here with the attributes, doesn't use the self parameter however
    make = ""
    model = ""
    year = 0

    def description(make, model, year): #The method is being defined here and is returned with the use of a foo bar
        return f"The car is a {make} with a {model} and made in {year}"

car = Car
car.make = input("Enter the make: ")
car.model = input("Enter the model: ")
car.year = int(input("Enter the year of the car: "))
print(car.description(car.make, car.model, car.year))

#Alternative Solution
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.make} {self.model} {self.year}"