#my solution
class Person:
    def __int__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
    
    def get_age_in_days(self):
        return self.age * 365
    
    def get_info(self):
        return ("Name: ", self.name, "Age: ", self.age, "Gender: ", self.gender, "email: ", self.email)

p = Person("Edwin", 17, "Male", "edrummer8247@gmail.com")
print(p.get_age_in_days())
print(p.get_info())

#Correct Solution
class Person:
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

    def get_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nEmail: {self.email}"

    def get_age_in_days(self):
        return self.age * 365

# Create an instance of the Person class and test its methods
person = Person("Alice", 30, "Female", "alice@example.com")
print(person.get_info())
print(person.get_age_in_days())