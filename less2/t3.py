a = input('>>> ').split()
try:
    a.append(a.pop(0))
except:
    print('[]')
finally:
    print(a)
