"""
Given a string. the task is to check if the string is symmetrical and palindrome or not.
A string is said to be symmetrical if both the halves of the string are the same and a string is said to be a palindrome string
if one half of the string is the reverse of the other half or if a string appears same when read forward or backward.

Example: 

Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome

Input: amaama
Output:
The entered string is symmetrical
The entered string is palindrome
"""

word = "khokho"
str_lth = len(word)
half = int(str_lth / 2)

if str_lth % 2 == 0:
    half_word = word[:half]
    other_half = word[half:]
    for i in range(0, half):
        if half_word[i] == other_half[i]:
            continue
        else:
            print("not a symmetric")
            break

    print("it is a symmeteric")
else:
    print("not a symmetric")

if word == word[::-1]:
    print("its a palindrome")
else:
    print("its not a palindrome")
"---------------------------------------------------------------------------------------------------------------------------------"

"""Given a range of numbers, print all palindromes in the given range. For example if the given range is {10, 115}, 
then output should be {11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111}
We can run a loop from min to max and check every number for palindrome. If the number is a palindrome, we can simply print it. 
"""

for i in range(10, 1000):
    if str(i) == str(i)[::-1]:
        print(i, " ")
    else:
        # print(i)
        pass


n = 2357887
new_num = 0
while n > 0:
    temp = n % 10
    new_num = new_num * 10 + temp
    print(new_num)
    n = n // 10
