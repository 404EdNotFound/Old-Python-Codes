# write a code which can be written in a similar way, properties name of a subject, mark, total marks, percentage, grade, student name. define class is Mount_St_Joseph, contrsuct a print statment showing all of the properties
class Mount_St_Joseph:
    studentName = ""
    name_of_subject = ""
    marks = 0
    totalMarks = 0
    percentage = 0.0
    grade = 0

    def description(a):
        desc_str = "%s is doing the subject %s. %s has got %d out of %d which is equivalent to %.1f percent and a grade %d" % (a.studentName, a.name_of_subject, a.studentName, a.marks, a.totalMarks, a.percentage, a.grade)
        return desc_str
student1 = Mount_St_Joseph()

student1.studentName = "Jeff"
student1.name_of_subject = "Maths"
student1.marks = 18
student1.totalMarks = 25
student1.percentage = (student1.marks / student1.totalMarks) * 100
student1.grade = 7

student2 = Mount_St_Joseph()

student2.studentName = "Bob"
student2.name_of_subject = "Science"
student2.marks = 26
student2.totalMarks = 41
student2.percentage = (student2.marks / student2.totalMarks) * 100
student2.grade = 6

print(student1.description())
print(student2.description())