class Student:
    def __init__(self,name,roll_no,age,gender) -> None:  #Constructor
    # This are called attributes 
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.gender = gender

    # def set_details(self,name,roll_no,age,gender):
    #     # self.name = input("Enter the name: ")
    #     # self.roll_no = int(input("Enter the roll no: "))
    #     # self.age = int(input("Enter the age: "))
    #     # self.gender = input("Enter the gender: ")

    #     self.name = name
    #     self.roll_no = roll_no
    #     self.age = age
    #     self.gender = gender

    def display_details(self):
        print(student1.name)
        print(student1.roll_no)
        print(student1.age)
        print(student1.gender)
#Object/Instances
student1= Student("Praveen",162,23,"Male")
# student1.set_details("Praveen",162,23,"Male")
student1.display_details()