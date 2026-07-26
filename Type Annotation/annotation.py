def is_add(a:int,b:int) -> int:
    return a + b
print(is_add(10,12))

def get_names(x:str , y:str) -> list:
    lst = []
    lst.append(x)
    lst.append(y)
    return lst
name1 = "Praveen"
name2 = "Raju"
ans = get_names(name1,name2)
print(ans)