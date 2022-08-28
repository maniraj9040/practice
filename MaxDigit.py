"""
You have a number and you need to determine which digit in this number is the biggest.

"""


def max_digit(number: int) -> int:
    d = 0

    while number > 0:
        n = number % 10
        a = max(n, d)
        d = a
        number = int(number / 10)

    return d


if __name__ == "__main__":
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
