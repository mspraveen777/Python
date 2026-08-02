# Deep Copy
import copy
original = [1,2,3,[23,43,56],34,56]
# shallow = original.copy()
# shallow[3][1] = 99
# print(shallow)
# print(original)  # here in both shallow $ original val changes bcz shallow will not
                  # work  in  nested mutuble collection 
#so we use deep copy

deep = copy.deepcopy(original)
deep[3][1] = 99
print(deep)       # here in original it will not change 
print(original)