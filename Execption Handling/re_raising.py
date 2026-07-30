def age_check():
    try:
        age = int(input("Enter the age: "))
        if age < 0:
            print("Age cannot be negative")
        elif age >= 150:
            print("Age is not real")

    except ValueError as e:
        print(f"Inside function Error = {e}")
        raise
    except Exception as e:
        print(f"Inside function Error = {e}")


try:
    age_check()
except Exception as e:
    print(f"Outside function Error = {e}")
else:
    print("success")
