import os

print(os.path.exists("append.py"))  # checks for both file and folder

print(os.path.isfile("new.txt"))  # checks for  file

print(os.path.isdir("Sets"))  # checks for both  folder

print(os.path.getsize("new.txt"))  # returns file size

print(
    os.path.join("data", "logs", "log.txt")
)  # joins all by "/'\ based on wind or linux
