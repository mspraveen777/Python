try:
    num = int(input("Enter the num: "))
    x = 10 / num
    print(f"x = {x}")
except ZeroDivisionError:
    print("Enter the proper Integer")
