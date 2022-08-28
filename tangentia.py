# problem 1
############
str1 = "ABC"
str2 = "DEF"

# out_str = "ADBECF"

out_str = "".join(i for j in zip(str1, str2) for i in j)

print(out_str)
##################################3

# problem 2
# =========
# If any two items in a list is equal to a given number

list1 = [10, 15, 3, 7, 13, 4, 17, 0]
n = 17

output = [0, 3]

for i in list1:
    a = n - i
    if a in list1:
        print([list1.index(i), list1.index(a)])
