# Shallow Copy 
import copy

original = [1,2,3]
# shallow = original.copy()           # Here id is differnt and only copy the reference
shallow = copy.copy(original)   # Another method
shallow.append(200)
print(shallow,id(shallow))
print(original,id(original))


