"""
Q67. Given a list of marks, use list comprehension to create a new list that contains
only the marks that are above 75.
"""
marks = [65,75,78,96,100,56,35,98,85,88]
marks_above_75 = [num for num in marks if num > 75]
print(marks_above_75)