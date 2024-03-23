def desk(x, y):
    global platform
    global y1
    y1 = y
    platform = [1 for _ in range(x)]
    print(platform)


def f():
    for _ in range(1, y1):
        for j in range(1, len(platform)):
            platform[j] += platform[j - 1]
    print(platform[-1])

desk(5, 3)
f()