"""
Reverse the sting
"""

text = "Praveen is a coder and learning python"
lst = text.split()
word_lst = lst[::-1]
print(lst[::-1])
res =" ".join(word_lst)
print(res, type(res))