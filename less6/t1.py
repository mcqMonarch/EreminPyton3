x, y = map(int, input('>>> ').split())
a = [[''] * y for _ in range(x)]
# for i in range(x):
#     for j in range(y):
#         a[i][j] = int(input())
a1 = []
a2 = []
for i in range(x):
    a[i] = list(map(int, input('>>> ').split()))
    if len(a[i]) != y:
        print('lol u noob')
        break
    a1.append(a[i])
for j in range(y):
    maxx = -1
    for i in range(x):
        if a[i][j] > maxx:
            maxx = a[i][j]
    a2.append(maxx)
for i in a1:
    for j in a2:
        if a1[i] == a2[j]:
            print(i, j)