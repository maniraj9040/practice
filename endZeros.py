"""
Try to find out how many zeros a given number has at the end.

"""


# method 1:


def end_zeros(num: int) -> int:
    count = 0
    for i in str(num)[::-1]:
        if i != str(0):
            break
        else:
            count += 1

    return count


if __name__ == "__main__":
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")


# method 2:
def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip("0"))
