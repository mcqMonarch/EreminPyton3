from copy import deepcopy

lst = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
print(id(lst[0][2]))
print(id(lst[1][0]))
lst[2][0] = 16
print(lst)
# lst2 = lst
# lst2 = deepcopy(lst)
lst2 = lst[::]
lst2[0].remove(lst2[0][0])
print(lst2)
print(lst)
