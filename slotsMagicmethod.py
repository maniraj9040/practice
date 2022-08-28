"""
When we create objects for classes, it requires memory and the attribute are stored in the form of a dictionary. 
In case if we need to allocate thousands of objects, it will take a lot of memory space.slots provide a special mechanism
to reduce the size of objects.It is a concept of memory optimisation on objects.

As every object in Python contains a dynamic dictionary that allows adding attributes. For every instance object, 
we will have an instance of a dictionary that consumes more space and wastes a lot of RAM. In Python,
there is no default functionality to allocate a static amount of memory while creating the object to store all its attributes.
Usage of __slots__ reduce the wastage of space and speed up the program by allocating space for a fixed amount of attributes.

"""


class Test(object):
    __slots__ = ["name"]

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    test = Test(name="mani")
    print(test.name)
    # test.age = 28
    # print(test.age)  # cannot add new variable as only name is defined in the __slots__
