"""Hirechal Inheritence- Here multiple child class inherit the propety from
one parent class
"""


class Animal:
    def sound(self):
        print("Animals makes their own sound")


class Dog(Animal):
    def bark(self):
        print("BOW BOW!")


class Cow(Animal):
    def Mows(self):
        print("ambaa ambaa")


class Cat(Animal):
    def Meow(self):
        print("Meow")


d = Dog()
d.sound()
d.bark()
