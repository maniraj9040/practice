class Car:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    @classmethod
    def red_cars(cls):
        # cls is the Car class
        # print(cls.color)
        print(cls)

    @staticmethod
    def blue_cars():
        # cls is the Car class
        # print(cls.color)
        print("a")
        return "b"


a = Car("Red")
print(a.get_color())
print(a.red_cars())
print(a.blue_cars())