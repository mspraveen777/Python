# # readline

# with open("abc.txt", "r") as f:
#     line1 = f.readline()
#     print(line1)
#     line2 = f.readline()
#     print(line2)


# readlines()

with open("abc.txt", "r") as f:
    lines = f.readlines()
    print(lines)

    for l in lines:
        print(l.strip())
