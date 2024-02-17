x, y = map(int, input('>>> ').split())
lst = [['1'] * y for _ in range(x)]
# for i in range(x):
#     for j in range(y):
#         if i < j:
#             lst[i][j] = '0'
#         elif i > j:
#             lst[i][j] = '2'
lst = [i for i in range(x)]
print('\n'.join(' '.join(i) for i in lst))