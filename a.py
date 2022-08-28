dList = [{"a": 1, "d": 1}, {"b": 3}, {"c": 5}]
for dic in dList:

    dic["a"] = 5


print(dList)


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:

            if self.left:
                print("left")
                self.left.insert(val)
                print("line 27", self.left)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            print("right")
            self.right.insert(val)
            print("line 34", self.right)
            return
        self.right = BSTNode(val)


b = BSTNode(10)
b.insert(15)
print(b.left)
print(b.right)
print(b.val)