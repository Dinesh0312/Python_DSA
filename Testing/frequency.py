lst = [4, 5, 1, 3, 4, 5, 5, 5, 3, 5, 6, 4, 6, 5, 5, 5, 4, 1, 3, 4, 4]
n = len(lst)

freq = {}

# for i in range(0, n):
#     freq[lst[i]] = lst.count(lst[i])

# print(freq)


for i in range(0, n):
    if lst[i] in freq:
        freq[lst[i]] += 1
    else:
        freq[lst[i]] = 1

print(freq)