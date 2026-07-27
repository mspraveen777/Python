# method overriding
class Animal:
    def speak(self):
        print("Animal is speaking...")


class Dog:
    def speak(self):
        print("Dog is Barking...")


d = Dog()
d.speak()
