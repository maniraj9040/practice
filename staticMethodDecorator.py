from unicodedata import name


class student:
    name = "unknown"

    def __init__(self) -> None:
        self.age = 20

    @staticmethod
    def tostring():
        print(student.name)


inst = student()
inst.tostring()
