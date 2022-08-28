import re


def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        # print(n)
        print("line first")
        recursiveMethod(n - 1)
        print("line second")
        print(n)


recursiveMethod(4)
print(" = " * 40)


def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n - 1)
        return power * 2


result = powerOfTwo(4)
print(result)