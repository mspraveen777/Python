# In case of mutable object
import copy
def is_add(x):
    x = copy.deepcopy(x)  # To overcome it we can use this
    x.append(100)
    print(f" Inside Function x = {x}")

num = [10,20,30]
is_add(num)
print(f" Outside Function num = {num}")         # here only the reference is passed
                                            # adress of num is passed so both changes 
                                            # to overcome it we can use copy