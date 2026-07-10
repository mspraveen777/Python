"""
Q61. Given a list, remove all duplicate elements while preserving the original
order of the unique items.
"""

def remove_duplicates(lst):
    new_lts = []
    lst.sort()
    n = len(lst)
    for i in range(1, n):
        if lst[i] not in new_lts:
            new_lts.append(lst[i])
    return new_lts
lst = [10,10,50,10,20,20,20,30,30,30]
ans = remove_duplicates(lst)
print(ans)
