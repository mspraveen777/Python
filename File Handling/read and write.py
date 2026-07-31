# # File handling

# f = open("abc.txt", "r")
# content = f.read(10)
# print(content)

# # f = open("abc.txt", "r")
# content1 = f.read(10)
# print(content1)
# # f = open("abc.txt", "r")
# content2 = f.read(10)
# print(content2)
# f.close()


with open("abc.txt", "r") as f:
    content = f.read(10)
    print(content)
    content1 = f.read(10)
    print(content1)
