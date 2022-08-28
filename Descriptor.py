"""_summary_
    Python descriptors are created to manage the attributes of different classes which use the object as reference.
    In descriptors we used three different methods that are __getters__(), __setters__(), and __delete__(). 
    If any of those methods are defined for an object, it can be termed as a descriptor.
    Normally, Python uses methods like getters and setters to adjust the values on attributes without any special processing.
    It’s just a basic storage system. Sometimes, You might need to validate the values that are being assigned to a value. 
    A descriptor is a mechanism behind properties, methods, static methods, class methods, and super().
"""
"""
Creating a Descriptor using class methods :
In this we create a class and override any of the descriptor methods __set__, __ get__, and __delete__.
This method is used when the same descriptor is needed across many different classes and attributes,
for example, for type validation.
"""


class Descriptor(object):
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        print("__get__")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("__set__")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print("__delete__")
        del instance.__dict__[self.name]


class Foo(Descriptor):
    name = Descriptor()

    def MethodA(self):
        print(self.name)


if __name__ == "__main__":
    obj = Foo(name="mani")
    print(obj.name)
    print(obj.MethodA())


# ========================================================================================
"""
Creating a Descriptor using @property Decorator :
In this we use the power of property decorators which are a combination of property type method and Python decorators.
"""


class Alphabet:
    def __init__(self, value):
        self._value = value

    # getting the values
    @property
    def value(self):
        print("Getting value")
        return self._value

    # setting the values
    @value.setter
    def value(self, value):
        print("Setting value to " + value)
        self._value = value

    # deleting the values
    @value.deleter
    def value(self):
        print("Deleting value")
        del self._value


# passing the value
x = Alphabet("Peter")
print(x.value)

x.value = "Diesel"

del x.value
