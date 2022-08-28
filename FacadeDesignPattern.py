"""
Façade is a structural design pattern which provides the simpler interface to a library or complex set of classes.
The word Façade is simply referred to an outer lying interface of complex patterns that contains several sub-systems.
"""


class Sensor:
    def __init__(self) -> None:
        pass

    def sensonOn(self):
        print("senson on")

    def sensonOff(self):
        print("senson off")


class Lights:
    def __init__(self) -> None:
        pass

    def lightsOn(self):
        print("senson on")

    def lightsOff(self):
        print("senson off")


class Smoke:
    def __init__(self) -> None:
        pass

    def smokeOn(self):
        print("senson on")

    def smokeOff(self):
        print("senson off")


class MetaClass(type):
    """This is a singleton design pattern"""

    _instance = {}

    def __call__(cls, *args, **kwds):
        """if instance already exists then don't create new one"""
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwds)
            return cls._instance[cls]


class Facade(metaclass=MetaClass):
    def __init__(self) -> None:
        self._sensor = Sensor()
        self._lights = Lights()
        self._smoke = Smoke()

    def Emergency(self):
        self._sensor.sensonOn()
        self._lights.lightsOn()
        self._smoke.smokeOn()

    def nonEmergency(self):
        self._sensor.sensonOff()
        self._lights.lightsOff()
        self._smoke.smokeOff()


if __name__ == "__main__":
    sensor = 22
    facade = Facade()
    print(facade)
    facade1 = Facade()
    print(facade1)
    if sensor > 30:
        facade.Emergency()
    else:
        facade.nonEmergency()

    # if sensor > 30:
    #     facade1.Emergency()
    # else:
    #     facade1.nonEmergency()
