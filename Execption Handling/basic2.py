try:
    num = int(input("Enter the num: "))
    x = 10 / num
    print(f"x = {x}")
except ZeroDivisionError:     # Good way of writing execption
    print("Enter the proper Integer")
