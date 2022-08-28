from array import *

from numpy import size

array1 = array("i", [10, 20, 30, 40, 50])
print(array1)


# add element at the end of an array
array1.append(60)

# insert element at an index in an array
array1.insert(1, 70)
array1.insert(1, 70)
array1.insert(1, 70)
array1.insert(1, 70)

# update the element at an index in an array
array1[2] = 80

# remove element from an array
array1.remove(30)

for x in array1:
    print(x)

print("=" * 40)
print(array1.index(40))

array1.remove(70)

print(array1.index(40))
