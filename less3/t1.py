def r(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    elif x == 3:
        return 1
    else:
        return r(x - 3) + r(x - 2) + r(x - 1)


print(r(9))
