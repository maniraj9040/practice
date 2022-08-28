# def extendList(val):
#     list.append(val)
#     return list


# list1 = extendList(10)
# list2 = extendList(12)
# list3 = extendList("a")
# print(list1, list2, list3)  # [10],[[123]],['a']


l1 = [2, 4, 2, 7, 7, 4, 7, 4, 7]

# method 1 : (simple)
print(max(set(l1), key=l1.count))

# method 2:
c = set(l1)
d = {}
for i in c:
    count = 0
    for j in range(0, len(l1)):
        if l1[j] == i:
            count += 1
    d[i] = count
print(d)


# method 3:
d = {}
for i in c:
    d[i] = l1.count(i)

print(d)


# method 4:
items = dict()
for item in l1:
    items[item] = items[item] + 1 if item in items else 1
print(max(items, key=items.__getitem__))
