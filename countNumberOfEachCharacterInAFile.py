import collections
import pprint

with open("/home/waterlabs/Documents/backup/lap_ref.txt", "r") as data:
    count_data = collections.Counter(data.read().upper())
    count_value = pprint.pformat(count_data)
# print(count_value)

a = "aksjdfhsnvijnjasdnfkjansdkjn"
count_data = collections.Counter(a)
count_value = pprint.pformat(count_data)
print(count_data)
print(count_value)


x = sorted((v, k) for k, v in count_data.items())
print(x)
print(x[-2][1])

print("=" * 40)


def add_nums(num1, num2):
    while num2 != 0:
        data = num1 & num2
        num1 = num1 ^ num2
        num2 = data << 1
    return num1


print(add_nums(2, 10))
