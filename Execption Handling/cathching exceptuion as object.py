try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    num = num1 / num2
    print(f"num = {num}")
except Exception as e:
    print(f"Error Message = {e}")
    print(f"Error type = {type(e).__name__}")
