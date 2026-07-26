class Student:
    School = "Excellent Public School"      #Class Variable

    def __init__(self,name:str) -> None:
        self.name = name

s1 = Student("Praveen")
s2 = Student("Raju")

print(s1.School)       # instance variable
print(s2.School)       # instance variable
print(Student.School)   

s1.School = "Royal Place School"    # changes in the school of s1
Student.School = "FPS School"       # changes school name of everyone in the class

print(s1.School)       # instance variable
print(s2.School)       # instance variable
print(Student.School)   