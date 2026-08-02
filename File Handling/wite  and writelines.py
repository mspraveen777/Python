# write

# with open("new.txt", "w") as f:
#     f.write("I am Praveen\n")
#     f.write("I am CS Graduate\n")


# writelines()
lines = ["I am Praveen\n", "ajshfjsdl\n", "hdfhd\n"]
with open("new.txt", "w") as f:
    f.writelines(lines)
