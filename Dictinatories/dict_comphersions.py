#Dictinaries Comphernsions
# squares = {}
# for i in range(1,11):
#     squares[i] = i*i
# print(squares)

# # comphernsion
# squares = {i:i*i for i in range(1,11)}
# print(squares)

#example
marks = {"maths":85,"science":92,"english":60,"hindi":45}
top = {sub:marks    for sub,marks in marks.items() if marks > 80}
print(top)
