student = {
    "name": "Praveen",
    "gender": "Male",
    "city": "Bengaluru",
    "age": 35
}
# print("name"in student)
# print(35 in student)  # It will only checks for keys


k = input("Enter the Key: ")
if k in student:
    print(student[k])
else:
    print("Key not found")