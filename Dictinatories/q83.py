"""
Q83. Subject Performance Analysis

Given a dictionary of marks for different subjects, loop over its values() to
calculate and print the total marks and the average mark obtained.
"""

marks = {
    "Science": 95,
    "Maths": 89,
    "Hindi": 88,
    "Computer Sciecne": 95,
}
# total = 0
# total_subjects = len(marks)
# for mark in marks.values():
#     total += mark

# average = total / total_subjects
# print(f"Total = {total} and Average = {average}")

# or else we can do like this

total_subjects = len(marks)
total = sum(marks.values())
average = total/total_subjects
print(f"Total = {total} and Average = {average}")
