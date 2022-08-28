"""
Split the string into pairs of two characters. If the string contains an odd number of characters,
then the missing second character of the final pair should be replaced with an underscore ('_').
"""

# method 1:


def split_pairs(a):
    return [ch1 + ch2 for ch1, ch2 in zip(a[::2], a[1::2] + "_")]


# method 2:
def split_pairs(a):
    b = [a[i : i + 2] for i in range(0, len(a), 2)]
    if len(a) % 2 == 1:
        b[-1] = b[-1] + "_"


if __name__ == "__main__":
    print("Example:")
    print(list(split_pairs("abcd")))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs("abcd")) == ["ab", "cd"]
    assert list(split_pairs("abc")) == ["ab", "c_"]
    assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
    assert list(split_pairs("a")) == ["a_"]
    assert list(split_pairs("")) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")