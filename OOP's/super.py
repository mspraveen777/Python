class Vehicle:
    def __init__(self, brand: str) -> None:
        print("This is vehicle constructor")
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand: str, fuel: str) -> None:
        super().__init__(brand)  # super keyword which prints __init__ of parent class
        self.fuel = fuel
        print("This is Car cosntructor")

    def car_display(self):
        print(f"You have {self.brand} car and {self.fuel} type")


v1 = Car("BMW", "petrol")
v1.car_display()
