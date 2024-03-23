import random

n = int(input('>>> '))
price = [0, 0] + [random.randint(1, 10) for i in range(n)]
print(price)
for i in range(1, n + 2):
    price[i] += min(price[i - 1], price[i - 2])
print(price)
