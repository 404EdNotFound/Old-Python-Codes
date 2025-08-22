#Examples of Classes and Objects
class MyClass:
    variable = "blah"
    variable2 = "Hello"

    def function(self):
        print("This is a message inside the class.")

#objects x, y and z are calling the class (MyClass)
myobjectx = MyClass()

myobjecty = MyClass()

myobjectz = MyClass()

# the variables in the classes are called by the variables which are calling the class
myobjectx.variable

myobjecty.variable2

# myobjecty.variable = "Hello"

# since the class doesn't have a print command, everything is printed here with the print command
print(myobjectx.variable)

print(myobjecty.variable2)

# print(myobjecty.variable)

# since the function has the print command, it doesnt need a print command after calling out the function
myobjectz.function()