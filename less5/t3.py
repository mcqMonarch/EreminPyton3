x, y = map(int, input('>>> ').split())
print([[j * i for j in range(y)] for i in range(x)])
