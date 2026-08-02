# method overriding
class Animal:
    def speak(self):
        print("Animal is speaking...")


class Dog:
    def speak(self):
        print("Dog is Barking...")


d = Dog()
d.speak()  # method speak from overrides the method speak from animal
