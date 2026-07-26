class Student:
    def __init__(self,name,roll_no,age,marks) -> None:
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}\nRoll_no: {self.roll_no}\nage: {self.age}" )

    def total(self):
        return sum(self.marks)

    def average(self):
         return sum(self.marks)/len(self.marks)
    def grade(self):
        avg = self.average()
        if avg > 90: return "A+"
        if avg >= 75: return "A"
        if avg >= 40: return "B"
        else: return "C"
Student1 = Student("Praveen",162,23,[100,99,89,75])
Student1.display_details()
Total = Student1.total()
print(f"Total: {Total}")
avg = Student1.average()
print(f"Average: {avg}")
grade = Student1.grade()
print(f"Grade: {grade}")



        