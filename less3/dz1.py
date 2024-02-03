import random

a = [random.randint(2, 10) for i in range(10)]
print(a)
# print(sorted(a, key=lambda x: (x % 3)))
x1 = x2 = []
for i in a:
    if i % 3:
        x1.append(i)
    else:
        x2.append(i)
x1.sort()
x2.sort()
# print(' '.join(x1), ' '.join(x2))
for i in x1:
    print(i, end=' ')
for i in x2:
    print(i, end=' ')
