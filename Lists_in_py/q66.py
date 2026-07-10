"""
Q66. Using list comprehension, create a list of squares of all odd numbers from 1 to 20.
"""

squares = [i**2 for i in range(1,21) if i%2 == 1]
print(squares)