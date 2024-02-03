import sys


def r(x):
    if x == 1:
        return 1
    else:
        return r(x - 1) * x


print(r(4000))
