# **Kwargs -- it allow u to any type name and value data type
# starts with **


def details(**kwargs):
    print(kwargs)
    print(type(kwargs))


details(name="Praveen", age=23, usn=162)
