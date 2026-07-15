"""
 Create a dictionary  Students, including name,age,city and marks. Print each piece 
 of information using it key.
 """
students = { "name":"Pravin","age":23,"city":"Bengaluru","marks":[100,89,95,88]}

for k in students:
    print(f"{k} = {students[k]}")
