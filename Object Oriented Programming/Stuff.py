class dog: #Class is defined with the keyword class which is reusable and allows the user to create objects
    def __init__(self, name, age): #This is a specific method with 2 underscores before and after 'init' this instantates the object and initialises it with the self parameter along with many other parameters
        self.name = name #Creates an attribute of the class with a permanent storing, many attributes can be created
        self.age = age
    #Method
    #def bark(self): #The function is defined inside the class as a method with the self parameter
        #print("Bark")

    #def add(self, x): #Methods can have multiple parameters / arguments
        #return x + 1  #Methods can also use reutrn which return to the method
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age): #This method doesn't require any returns but has more paramters that are needed to pass through and affect the current value that had been stored under the attribute
        self.age = age

'''
d = dog("name", 5) #Calls the class with a variable (where the object is created) as a new instance, many parameters can be added and passed through
d.set_age(2) #Used to change the value that has already been stored in the atrribute
doggy = dog("names", 7) #Multiple classes can be created to be reused
print(d.get_name(), d.get_age(), doggy.get_name(), doggy.get_age()) #Placing an attribute/method and calling it can be used as reference

#print(type(d)) #Displays the type of class added

#d.bark() #Calls the method with instantating variable
#print(d.add(5)) #When calling a class or method, a parameter can be assigned here for passing
'''

