class Test(object):
    myvar = 2222

    def __init__(self, num=1):
        self._number = num

    # number is a private, hence to access it outsid the class you need to create set and get methods
    def get(self):
        # can return private variables outside the class
        return self._number

    def set(self, num):
        # can set private or protected variables from outside of the class
        self._number = num

    @property
    def propertymethod(self):
        print("i am propertymethod function, you can call me witout using brackets")

    @staticmethod
    def staticFunction():
        # print(myvar)  raise an error "NameError: name 'myvar' is not defined", as static methods do not have class status
        print("i am static method")

    @classmethod
    def classFunction(cls):
        print("class variable access {}".format(cls.myvar))

    def __str__(self) -> str:
        return "object class"


if __name__ == "__main__":
    obj = Test()
    print(obj)
    print(obj.get())
    print(obj.set(123))
    print(obj.get())
    print(obj.propertymethod)
    print(Test.staticFunction())
    print(obj.classFunction())
