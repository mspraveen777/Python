# Mutating 

def mutate(x):
    # x.append(1) 
    x[0] = 1  #mutating  here it mutate or changes the orginal value
    print(f" Inside the fucnction = {x}")

num = [10,20,30]  
mutate(num)     
print(f"Outside the function = {num}")