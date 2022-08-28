"""
The factory pattern comes under the creational patterns list category. 
It provides one of the best ways to create an object. In factory pattern, objects are created without exposing 
the logic to client and referring to the newly created object using a common interface.

Factory patterns are implemented in Python using factory method. 
When a user calls a method such that we pass in a string and the return value as a new object is
implemented through factory method. The type of object used in factory method is determined by string which 
is passed through method.
"""


class A(object):
    def __init__(self) -> None:
        pass

    def methodA(self):
        print("A")


class B(object):
    def __init__(self):
        pass

    def methodB(self):
        print("B")


def get(obj=""):
    objs = dict(a=A(), b=B())
    return objs[obj]


f = get("a")
print(f)

g = get("b")
print(g)
