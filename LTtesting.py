from cgi import print_directory
from subprocess import list2cmdline
import collections


def extendList(val, list=[]):
    list.append(val)
    return list, id(list)


list1 = extendList(10, [])
list2 = extendList(123)
list3 = extendList("a")
print(list1)
print(list2)
print(list3)


a = 20
print(a, id(a))
b = a
b = 7
print(a, id(a))
print(b, id(b))

a = 10
print(a, id(a))
print(b, id(b))

print("&" * 40)

l1 = [2, 4, 2, 7, 7, 4, 7, 4, 7]
c1 = {}
c = []
for i in l1:
    if i in c:
        print(c)
        c1[i] += 1
    else:

        c1[i] = 1
        c.append(i)

print(c1)
print(c)

print("&" * 40)
a = collections.Counter(l1)

print(sorted((i, j) for i, j in a.items())[-1][0])
