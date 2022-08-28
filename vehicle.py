class automobile:
    pass


class vehicle(automobile):
    def __init__(self, name, speed, mileage, capacity) -> None:
        self.name = name
        self.max_speed = speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare(self):
        return self.capacity * 100


class Bus(vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount


class Car(vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


school_bus = Bus("School volvo", 180, 12, 50)
print(
    "vehicle bus: ",
    school_bus.name,
    "speed: ",
    school_bus.max_speed,
    "mileage: ",
    school_bus.mileage,
)
print(school_bus.seating_capacity())
print("bus fare : ", school_bus.fare())
print(type(school_bus))
print(isinstance(school_bus, automobile))
