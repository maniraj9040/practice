"""
There are 3 methods we can create  a class
"""

# method 1
from matplotlib.pyplot import cla


class A(object):
    def __init__(self):
        pass


# method 2
class B(object):
    def __call__(cls, *args, **kwds):
        # it is similar to method 3, call method calls new and init methods
        return super(B, cls).__call__(cls, *args, **kwds)


# method 3
class C(object):
    def __new__(cls, *args, **kwargs):
        # new create a memory of the class in the Heap memory"
        print("creating an object")
        return super(C, cls).__new__(
            cls,
        )

    def __init__(self, *args, **kwargs):
        # create a instance of the class
        print("creating instance of a class")
        super(C, self).__init__(*args, **kwargs)


a = A()
print(a)
b = B()
print(b)
c = C()
print(c)
