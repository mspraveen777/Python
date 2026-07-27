# Encapsulation
class BankAccount:
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        # self.balance = balance  # Public Attribute
        # self._balance = balance  # Protectd Attribute
        self.__balance = balance  # Private Attribute

    def deposit(self, amount: int):
        if amount <= 0:
            print("Invalid")
        else:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


b1 = BankAccount("Pravin", 1000)
print(b1.name)
print(b1.get_balance())

b1.deposit(500)
print(b1.get_balance())
# print(b1.__balance)        # it will throw error
