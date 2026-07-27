class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is staring...")


class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} is driving")


v1 = Car("Toyoto")
v1.start()
v1.drive()
