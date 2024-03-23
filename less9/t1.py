import random


def f(n):
    global cost
    cost = [price[0], price[1]]
    for i in range(2, n):
        cost.append(price[i] + min(cost[i - 1], cost[i - 2]))
    print(cost)


def way(price, cost):
    way_lst = []
    price = price[:len(cost)]
    print('цены:', price)
    i = len(cost)
    while i > 0:
        way_lst.append(i)
        # i -= 1
        if cost[i - 2] > cost[i - 1]:
            i -= 1
        else:
            i -= 2
    way_lst.append(0)
    print(way_lst[::-1])

price = [0] + [random.randint(-10, 10) for i in range(random.randint(20, 100))]
print(price)
f(5)
way(price, cost)