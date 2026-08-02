"""
Q103. Username Validation

Take a username as input. Strip any spaces from both sides and check if the
cleaned name starts with a letter (not a digit). Print "Valid" or "Invalid".
"""

def username_validation(name):
    name = name.strip()
    if name[0].isdigit():
        return "Invalid"
    return "Valid"
username = " Praveen "
print(username_validation(username))