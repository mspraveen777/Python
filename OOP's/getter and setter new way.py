class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.__age = age

    # getter  - new way
    @property
    def age(self1) -> int:
        return self1.__age

    # setter - new way
    @age.setter
    def age(self1, new_age: int):
        if new_age > 0:
            self1.__age = new_age


s1 = Student("Pravin", 23)
print(s1.age)  # we not supposed to write the braces
s1.age = 25
print(s1.age)
