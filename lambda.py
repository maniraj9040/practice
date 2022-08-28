########### using map function #########################

from math import lgamma


fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
result = map(lambda x: True if x[0] == "A" else False, fruit)
print(type(result))
print(result)
print(list(result))

print("=" * 40)
########### using filter function #########################

result = filter(lambda x: True if x[0] == "A" else False, fruit)

print(type(result))
print(result)
print(list(result))

print("=" * 40)

########### using reduce function #########################


from functools import reduce

list = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, list))
print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))