def desk(x, y):
    global platform
    global y1
    global b
    y1 = y
    platform = [1 for _ in range(x)]
    print(platform)
    b = ((1, 1), (2, 1))


def f():
    for i in range(1, y1):
        for j in range(1, len(platform)):
            platform[j] += platform[j - 1]
            if (j, i) in b:
                platform[j] = 0
            print(platform)
    print(platform[-1])


desk(5, 3)
f()