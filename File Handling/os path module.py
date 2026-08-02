import os

print(os.path.exists("append.py"))  # checks for both file and folder

print(os.path.isfile("new.txt"))

print(os.path.isdir("Sets"))

print(os.path.getsize("new.txt"))

print(os.path.join("data", "logs", "log.txt"))
