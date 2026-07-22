"""
Q97. Email Validation

Take an email as input. Validate that it contains exactly one @ and at least
one .
Print "Valid" or "Invalid".
""" 
def check_email(email):
     
    if email.count("@")==1 and "." in email:
        return "Valid"
    return "Invalid"
ans = check_email("mspraveen7@777@gmail.com")
print(ans)
