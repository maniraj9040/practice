class Parent:
    def __init__(self, fname, fage):
        self.firstname = fname
        self.age = fage

    def view(self):
        print(self.firstname, self.age)


class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)
        self.lastname = "edureka"

    def view(self):
        print(
            "course name",
            self.firstname,
            "first came",
            self.age,
            " years ago.",
            self.lastname,
            " has courses to master python",
        )


ob = Child("Python", "28")
ob.view()