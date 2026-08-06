# # readline

# with open("abc.txt", "r") as f:
#     line1 = f.readline()
#     print(line1)
#     line2 = f.readline()
#     print(line2)


# readlines()

with open("abc.txt", "r") as f:
    lines = f.readlines()  # if the lines are more list takes more storage it is not
    print(lines)  # optimized way

    for l in lines:
        print(l.strip())
