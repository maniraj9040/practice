"""
A metaclass in Python is a class of a class that defines how a class behaves. 
A class is itself an instance of a metaclass. A class in Python defines how the instance of the class will behave.
"""


class MetaClass(type):
    """This is a singleton design pattern"""

    _instance = {}

    def __call__(cls, *args, **kwds):
        """if instance already exists then don't create new one"""
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwds)
            return cls._instance[cls]


class A(metaclass=MetaClass):
    def __init__(self):
        pass


a = A()
print(a)
b = A()
print(b)
