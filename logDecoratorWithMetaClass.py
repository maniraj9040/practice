from email import message
from sympy import im


try:
    import os
    import datetime
    import logging
    import sys
except Exception as e:
    print("missing some modules {}".format(e))


class MetaClass(type):
    """Meta class"""

    def __call__(cls, *args, **kwds):
        instance = super(MetaClass, cls).__call__(*args, **kwds)
        return instance

    def __init__(cls, name, base, attr):
        super(MetaClass, cls).__init__(name, base, attr)


class log(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwds):
        """wrapper function"""

        start = datetime.datetime.now()
        funcName = self.func.__name__
        tem = self.func(*args, **kwds)
        end = datetime.datetime.now()

        message = """
        function : {},
        Execution time : {}
        Address : {}
        size of function : {}
        Date : {}
        """.format(
            funcName, end - start, self.func.__name__, sys.getsizeof(self.func), start
        )

        print(message)
        cwd = os.getcwd()
        folder = "logs"
        newPath = os.path.join(cwd, folder)

        try:
            os.mkdir(newPath)
        except:
            """folder already exists"""

            logging.basicConfig(
                filename="{}/log.log".format(newPath), level=logging.DEBUG
            )
            logging.debug(message)

        return tem


class Test(metaclass=MetaClass):
    def __init__(self, *args, **kwds):
        pass

    # note: in order to run logger the function has to be static hence changing the behavious using Meta class
    @log
    def methodA():
        print("method A")
        return "111"


if __name__ == "__main__":
    obj = Test()
    print(obj.methodA())
