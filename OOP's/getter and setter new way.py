class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.__age = age

    # getter  - new way
    @property
    def age(self) -> int:
        return self.__age

    # setter - Traditional way
    @age.setter
    def age(self, new_age: int):
        if new_age > 0:
            self.__age = new_age


s1 = Student("Pravin", 23)
print(s1.age)
s1.age = 25
print(s1.age)
