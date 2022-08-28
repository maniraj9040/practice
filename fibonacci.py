a = 100
b = 0
c = 1

if a > 0:
    if a == 1:
        print("answer is ", 1)

    for i in range(0, a):
        # print(i, " ", b)
        d = b + c
        b = c
        c = d

print("=" * 40)
## generate fibonacci numbers upto n
def fib(n):
    p, q = 0, 1
    while p < n:
        yield p
        p, q = q, p + q


x = fib(7)
print(x)
# x.__next__()


## iterating using loop
for i in fib(10):
    print(i)
