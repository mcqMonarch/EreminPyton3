import random


def m(lst1, lst2):
    # print(lst1, '|', lst2)
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    result = []
    while True:
        if lst1[0] > lst2[0]:
            result.append(lst2.pop(0))
        else:
            result.append(lst1.pop(0))
        if len(lst1) == 0:
            result += lst2
            break
        if len(lst2) == 0:
            result += lst1
            break
    return result


def m_sort(lst):
    if len(lst) >= 2:
        return m(m_sort(lst[:len(lst) // 2]), m_sort(lst[len(lst) // 2:]))
    else:
        return lst


x = [random.randint(-10, 10) for i in range(5)]
print(x)
print(m_sort(x))
