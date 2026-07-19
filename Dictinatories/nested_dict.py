#Nested Dictinaries

students = {"101":{"name":"Pravin","age":23,"city":"Benagluru"},
            "102":{"name":"Rahul","age":22,"city":"Hyderabad"},
            "103":{"name":"Suraj","age":21,"city":"Pune"},
            }
# print(students["101"])
# print(students["103"]["name"])
# print(students["103"]["Details"]["gender"])

# Acessing
for  roll_no,details in students.items():
    # print(f"Roll no: {roll_no} and Details: {details}")
    print(f"Roll no: {roll_no} and name: {details["name"]} and city: {details['city']}")