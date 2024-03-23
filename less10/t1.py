def desk(x: int, y: int):
    global platform, b
    # platform = [[1] * x] * y             Нельзя так дегрот
    platform = [[1 for _ in range(x)] for _ in range(y)]
    show()
    b = [[1 for _ in range(5)] for _ in range(3)]
    b[1][1] = 0
    b[2][1] = 0
    print('-----------')


def show():
    for i in platform:
        print(' '.join(str(j) for j in i))


def f():
    for i in range(1, len(platform)):
        for j in range(1, len(platform[0])):
            platform[i][j] = (platform[i - 1][j] + platform[i][j - 1]) * b[i][j]
    show()


b = [[1 for _ in range(5)] for _ in range(3)]
desk(5, 3)
f()
