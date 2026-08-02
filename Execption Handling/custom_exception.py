class InsufficientFunds(Exception):  # To create the custom execption
    pass


def withdraw_money(balance, withdrawl_amount):
    if withdrawl_amount > balance:
        raise InsufficientFunds("Not enough money")
    print(f"Remaining balance = {balance - withdrawl_amount}")


try:
    withdraw_money(1000, 5000)
except InsufficientFunds as e:
    print(f"Error name = {type(e).__name__}")
    print(f"Error = {e}")
except Exception as e:
    print(f"Error name = {type(e).__name__}")
    print(f"Error = {e}")
