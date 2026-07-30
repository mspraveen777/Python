try:
    num = int(input("Entet the num: "))
    x = 100 / num
except ValueError:
    print("ValueError Enter the proper type of Integer")
except ZeroDivisionError:
    print("ZeroDivisionError Enter Proper Integer")
else:
    print(f"x = {x}")
finally:
    print("Calculation Completed")
