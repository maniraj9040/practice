def lowercase_decorator(function):
    print("5")

    def wrapper():
        print("7")
        func = function()
        print("6")
        string_lowercase = func.lower()
        return string_lowercase

    return wrapper


# decorator function to split words
def splitter_decorator(function):
    print("2")

    def wrapper():
        print("3")
        func = function()
        print("4")
        string_split = func.split()
        return string_split

    return wrapper


@splitter_decorator  # this is executed next
@lowercase_decorator  # this is executed first
def hello():
    print("1")
    return "Hello World"


output = hello()
print(output)
print("#" * 10)
for i in range(1, 10, 2):
    print(i)