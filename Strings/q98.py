"""
Q98. Clean Phone Number

Take a phone number as input in the format +91-98765-43210. Remove all dashes
and the country code. Print the cleaned 10-digit number.
"""

def clean_phn_no(Phn):
    clened_no = Phn.split("-")
    return "".join(clened_no[1:])
Phn ="+11-12345-43247"
print(clean_phn_no(Phn))


