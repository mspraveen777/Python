# # For Loop

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


for i in range(5, 0, -1):
    for j in range(5, 5 - i + 1, -1):
        print(" ", end=" ")
    for k in range(5, i - 1, -1):
        print(k, end=" ")
    print()
# for i in range(5,0,-1):
#     for j in range(5,5-i+1,-1):
#         print(j,end=" ")
#     print()
