#Example of Object Oriented Programming

class Student: #Class is being defined here
    def __init__(self, name, age, grade): #initialises the class with provided parameters / arguments which the user can create attributes from
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self): #Used to catch one of the attributes and returns it to the method
        return self.grade

#Another class is created
class subject:
    def __init__(self, name, maximum):
        self.name = name
        self.maximum = maximum
        self.students = [] #attributes can be defined and assigned to something else rather than a direct assignment to the argument

    def addStudent(self, student): #Sometimes parameters may not be an attribute
        if len(self.students) < self.maximum:
            self.students.append(student)
            return True #Returns the statement
        return False
    
    def average(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

#Multiple objects are created with passing parameters
student1 = Student("Name", "Age", 1)
student2 = Student("Name2", "Age2", 2)
student3 = Student("Name3", "Age3", 3)

Subject = subject("Name", 30)
Subject.addStudent(student1)
Subject.addStudent(student2)
print(Subject.addStudent(student3))
print(Subject.average())