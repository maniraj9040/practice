import time
import random

# a = [1, 2, 4, 34, 6, -75, -8, 23, 55]
a = random.sample(range(1, 100), 99)

# normal way of sorting

countValue = 0
s = time.time()

for i in range(len(a)):
    for j in range(i + 1, len(a)):

        countValue += 1
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
e = time.time()
print("time taken ", e - s)
print(a, countValue)

print("#" * 40)
# sorting using insertion sorting alogrithm #
# a = [1, 2, 4, 34, 6, -75, -8, 23, 55]
a = random.sample(range(1, 100), 99)

countvalues = 0
s = time.time()
for i in range(1, len(a)):
    key = a[i]
    j = i - 1

    while j >= 0 and key < a[j]:
        countvalues += 1
        a[j + 1] = a[j]
        j = j - 1

    a[j + 1] = key
e = time.time()
print("time taken ", e - s)

print(a, countvalues)
