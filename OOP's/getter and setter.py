class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.__age = age

    # getter  - Traditional way

    def get_age(self) -> int:
        return self.__age

    # setter - Traditional way
    def set_age(self, new_age: int):
        if new_age > 0:
            self.__age = new_age


s1 = Student("Pravin", 23)
print(s1.get_age())
s1.set_age(25)
print(s1.get_age())
