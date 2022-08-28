from copy import copy, deepcopy

list_1 = [1, 2, [3, 5], 4]

print(list_1)
list_2 = copy(list_1)

print(id(list_1[0]), id(list_2[0]))
list_2[1] = 4
list_2[2].append(8)
print("list_1 :", list_1)

print("list_2 :", list_2)
list_3 = deepcopy(list_1)
list_3[1] = 10
list_3[2].append(9)
print(id(list_1), id(list_2), id(list_3))

print("list_1 :", list_1)

print("list_3 :", list_3)