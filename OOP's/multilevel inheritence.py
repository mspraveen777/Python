# MutliLevel Inhertence


class Animal:
    def breathe(self):
        print("It will breathe")


class Mammals(Animal):
    def fee_young_one(self):
        print("It will feed their young ones")


class Dog(Mammals):
    def sound(self):
        print("Barks: BOW BOW!")


d1 = Dog()
d1.sound()
d1.fee_young_one()
d1.breathe()
