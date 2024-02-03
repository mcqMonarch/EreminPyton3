a = input('>>> ').split()
if len(a):
    a.append(a.pop(0))
print(a)
