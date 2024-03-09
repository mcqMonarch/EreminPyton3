def fib(n):
    if n == 1 or n == 0:
        return n
    return fib(n - 1) + fib(n - 2)


def fib2(n):
    lst = [0] * (n + 1)
    lst[1] = 1
    for i in range(2, n + 1):
        lst[i] = lst[i - 1] + lst[i - 2]
    print(lst)


# print(fib(3))
def fib3(n):
    lst = [0] * 2
    lst[1] = 1
    for _ in range(n):
        lst[0], lst[1] = lst[1], lst[0] + lst[1]
    print(lst[0])


fib2(3)
fib3(3)
