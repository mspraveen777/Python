# Multiple


class swim:
    def swimming(self):
        print("It will swim")


class fly:
    def flying(self):
        print("It will fly")


class Duck(swim, fly):
    def quack(self):
        pass


d1 = Duck()
d1.swimming()
d1.flying()
