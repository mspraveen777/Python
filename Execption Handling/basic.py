try:
    age = int(input("Enter the number: "))
    if age >= 18:
        print("Adult")
    else:
        print("Not Adult")
except:
    print("Some error Occured")
print("Done")
