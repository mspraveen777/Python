"""
Q84. Top Scorers

Populate a dictionary with six student names and their corresponding marks.
Loop through it and print the names of all students who achieved a score above 75.
"""

students = {
    "Pravin": 100,
    "Akash": 99,
    "Raju": 57,
    "Suraj": 75,
    "Rahul": 72,
    "Shivu": 88,
}

for name,marks in students.items():
    if marks > 75:
        print(name)
        
