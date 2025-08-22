#Vehicle is being defined as a class description is being defined as a function followed by the self parameter
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    # description is being defined as a function followed by the self parameter
    def description(a):
        desc_str = "%s is a %s %s worth $%.2f." % (a.name, a.color, a.kind, a.value)
        return desc_str
# your code goes here

#car1 is calling the class Vehicle and its also calling out the variable in the class
car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "Red"
car1.value = 60000.00

#car2 is calling the class Vehicle and its also calling out the variable in the class
car2 = Vehicle()
car2.name = "Jump"
car2.kind = "Van"
car2.color = "Blue"
car2.value = 10000.00

# test code

#car1 and car2 is printing the function "description" and it prints out "desc_str" becuase the string and values are returned to the function until that function is called.
print(car1.description())
print(car2.description())

