# Rebinding 

def rebind(x):
    x = [100,200,300]   #rebinding
    print(f" Inside the fucnction = {x}")

num = [10,20,30]  # Here eventhough it is mutable object it does not change the 
rebind(num)     # bcz we rebind using = operator
print(f"Outside the function = {num}")