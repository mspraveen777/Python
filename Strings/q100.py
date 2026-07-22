"""
Q100. Sorted Names

Take a list of names as input (comma separated). Split them, sort them
alphabetically, and join them back with " | " as separator.
"""

def sorted_names(names):
    names = names.split(",")
    names = sorted(names)
    names =" | ".join(names)
    return names

names = "Praveen,Anirudh,Rahul,Mahesh"
print(sorted_names(names))