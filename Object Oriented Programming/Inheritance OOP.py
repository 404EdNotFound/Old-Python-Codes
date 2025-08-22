class Animals: #Class is created
    def __init__(self, name, age): #Initialises the class with given parameters / attributes
        #Attributes are defined here
        self.name = name
        self.age = age
    
    #The Method is defined here
    def show(self):
        print("I am", self.name, "and I am", self.age, "years old")
    
    def speak(self):
        print("I don't speak")

class Dog(Animals): #Class is created with an inheritance paramater
    """
    def __init__(self, name, age): #Initialises the class with given parameters / attributes
        #Attributes are defined here
        self.name = name
        self.age = age
    """
    
    #The Method is defined here
    def speak(self):
        print("Woof")

class Cat(Animals): #Class is created with an inheritance parameter

    def __init__(self, name, age, colour): #Initialises the class with given parameters / attributes
        #Attributes are defined here
        super().__init__(name, age) #super means superclass that is inherited from with the paramters to pass through
        self.colour = colour

    #The Method is defined here
    def speak(self):
        print("Meow")
    
def show(self):
        print("I am", self.name, "and I am", self.age, "years old and I am", self.colour)

animal = Animals("Edwin", 17)
animal.speak()

cat = Cat("Bill", 20, "White")
cat.show()

dog = Dog("Leg", 43)
dog.speak()