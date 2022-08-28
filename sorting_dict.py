# Function calling
def dictionairy():

    # Declaring hash function
    key_value = {}

    # Initializing the value
    key_value["a"] = 56
    key_value["z"] = 2
    key_value["r"] = 12
    key_value["t"] = 24
    key_value["c"] = 18
    key_value["f"] = 323

    print("Task 3:-\nKeys and Values sorted", "in alphabetical order by the value")

    # Note that it will sort in lexicographical order
    # For mathematical way, change it to float
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))[0])


def main():
    # function calling
    dictionairy()


# main function calling
if __name__ == "__main__":
    main()


"""
Ways to sort list of dictionaries by values in Python – Using itemgetter
"""

from operator import itemgetter
from webbrowser import get

lis = [
    {"name": "maniraj", "age": 27},
    {"name": "swathi", "age": 20},
    {"name": "shashirani", "age": 50},
    {"name": "saikrishna", "age": 30},
    {"name": "lavanya", "age": 28},
    {"name": "saanvi", "age": 1},
]

print(sorted(lis, key=itemgetter("age")))
print(sorted(lis, key=itemgetter("age"), reverse=True))
print(sorted(lis, key=itemgetter("age", "name")))


"""
    Let’s see how to combine the values of two dictionaries having same key.

"""


lis2 = {
    "maniraj": 27,
    "swathi": 20,
    "shashirani": 50,
    "saikrishna": 30,
    "lavanya": 28,
    "saanvi": 1,
}


lis3 = {
    "maniraj": 27,
    "swathi": 20,
    "shashirani": 50,
    "saikrishna": 30,
    "lavanya": 28,
    "saanvi": 1,
}

# print(lis2 + lis3)   //TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

from collections import Counter

ini_lis2 = Counter(lis2)
ini_lis3 = Counter(lis3)

final_list = ini_lis2 + ini_lis3
print(final_list)


# "using dict comprehension"
print("=" * 40)

final_list = {x: lis2.get(x, 0) + lis3.get(x, 0) for x in set(lis2).union(lis3)}
print(final_list)