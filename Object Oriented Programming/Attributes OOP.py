class person:
    num_people = 0 #Class attribute without self paramter
    GRAVITY = 9.8
    
    def __init__(self, name): #Methods are defined here
        self.name = name
        #person.num_people += 1 #increments the value without self parameter
        person.add_person()
        
    @classmethod #Decorator is used to idenfity a class method to reference the class rather than the self paramter
    def num_people1(cls): #cls is a statical method that is used to set limits
        return cls.num_people
    
    @classmethod
    def add_person(cls):
        cls.num_people += 1
person1 = person("Name")
person2 = person("Name2")

print(person.num_people1())
#person.num_people = 8 #The attribute can be changed when the class is called
#print(person2.num_people) #This calls the attribute while an object is created and checks if the attribute is in the class and if its labelled as a self parameter