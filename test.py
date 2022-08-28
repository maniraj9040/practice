a = [1, 5, 6, 3, 2, 7, 11, 66, 33, 88, 55, 99]

# for i in range(1, len(a)):
#     if (i % 2) == 0:
#         a[i] = "A"
#     else:
#         pass
# print(a)

for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
# a.sort()
print(a)


strs = ["geeks", "code", "ide", "practice"]
strs.sort()
print(strs)

b = [1, 5, 6, 3, 2, 7, 11, 66, 33, 88, 55, 99]
# b[::2] = "a"
# count = 1
# for i in range(1, len(a)):
#     if i % 3 == 0:
#         b[i] = "A"
# print(b)
# print(b[::2])


Tv = {"BreakingBad": 100, "GameOfThrones": 1292, "TMKUC": 88}

print("aaa", sorted((x, y) for x, y in Tv.items()))


# keymax = zip(Tv.values(), Tv.keys())

Keymax = max(Tv, key=lambda x: Tv[x])
print(Keymax)

import collections

od = collections.OrderedDict(sorted(Tv.items()))
print(od)
# print(sort((od.values())
print(list(od.keys()))