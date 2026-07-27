# Inheritence


class Animal:
    def __init__(self, name, sound) -> None:
        self.name = name
        self.sound = sound

    def eating(self):
        print(f"{self.name} is eating")

    def speak(self):
        print(f"{self.name} is {self.sound}..")


class Dog(Animal):
    pass


a1 = Dog("Dog", "Barking")
a1.eating()
a1.speak()
