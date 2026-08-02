try:
    with open("ne1w.txt", "r") as f:
        con = f.read()
        print(con)

except FileNotFoundError as e:
    print("File not found in dir")
except Exception as e:
    print("Some error occured")
