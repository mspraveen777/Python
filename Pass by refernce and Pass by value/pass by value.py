# In case of immutable object
def is_add(x):
    x = x+1
    print(f" Inside Function x = {x}")

num = 10
is_add(num)
print(f" Outside Function num = {num}")         # here only the value is passed