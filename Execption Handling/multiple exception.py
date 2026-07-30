try:
    num = int(input("Enter the num: "))
    x = 10 / num
    print(f"x = {x}")
except ValueError:
    print("Plz  enter the propet Integer")
except ZeroDivisionError:
    print("Cant divide by zero , enter the proper Integer")
