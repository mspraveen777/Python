try:
    num = int(input("Entet the num: "))
    x = 100 / num
except ValueError:
    print("ValueError Enter the proper type of Integer")
except ZeroDivisionError:
    print("ZeroDivisionError Enter Proper Integer")
else:           # else will run only try succed
    print(f"x = {x}")
finally:                    # finally will run compulsory
    print("Calculation Completed")
