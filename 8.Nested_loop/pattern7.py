"""

        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

"""
# n = 8

# for i in range(1, n + 1):
#     for j in range(n - i + 1):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print(k, end=" ")
#     print()


for i in range(1, 6):
    for j in range(5 - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()
for i in range(4,0,-1):
    for j in range(5 - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()


for i in range(1, 6):
    for j in range(5 - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()