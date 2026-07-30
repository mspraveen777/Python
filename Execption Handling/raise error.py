def check_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    elif age > 150:
        raise ValueError("Age is not real")
    else:
        print("Age is good")


check_age(-200)
