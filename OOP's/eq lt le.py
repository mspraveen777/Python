class Money:
    def __init__(self, amount) -> None:
        self.amount = amount

    def __eq__(self, other) -> bool:
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount


a = Money(80)
b = Money(100)
print(a == b)
print(a < b)  # it is not supported but using dunder we can do it
print(a <= b)  # it is not supported but using dunder we can do it

# Similarly we can do it for ge and gt
