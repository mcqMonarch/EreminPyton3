import random


def i_sort(lst: list):
    for i in range(1, len(lst)):
        j = 0
        while j < i and (lst[i] > lst[j]):
            j += 1
        lst.insert(j, lst.pop(i))
    print(lst)


x = [random.randint(-10, 10) for i in range(10)]
print(x)
i_sort(x)
