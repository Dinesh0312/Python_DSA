"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
"""
for i in range(5,0,-1):
    for j in range(i,5+1):
        print(j,end=" ")
    print()

"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""

for i in range(5,0,-1):
    for k in range(5,i-1,-1):
        print(k,end=" ")
    print()
print()
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

"""
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""

for i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
    print()

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
num = 1
for i in range(1,6):
    for j in range(i):
        print(num,end=" ")
        num = num + 1
    print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""
for i in range(5,0,-1):
    for j in range(i,5+1):
        print(j,end=" ")
    print()
for i in range(1,5):
    for j in range(i+1,6):
        print(j,end=" ")
    print()

"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()
for i in range(1,5):
    for j in range(5,i,-1):
        print(j,end=" ")
    print()