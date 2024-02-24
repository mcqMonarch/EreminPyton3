import random
import time


def b_sort(lst):
    for j in range(len(lst)):
        isready = True
        for i in range(len(lst) - 1 - j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                isready = False
        if isready:
            break


lst = [random.randint(-100, 100) for i in range(5000)]
# print(lst)
t_s = time.time()
b_sort(lst)
t_f = time.time()
print(t_f - t_s)
# print(lst)
