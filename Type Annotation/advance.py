def get_marks(a:list[int]):
    print(a)
get_marks([10,20,30,40])

def is_list(a:list[int | str])  -> list[int|str]:
    return a
ans = is_list([10,20,"Pravin"])
print(ans)