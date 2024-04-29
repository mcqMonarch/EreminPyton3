import fnmatch

a = ['a', '@b', 'c', 'a@', 'a', 'c']
print(sorted(a, key=lambda x: '@' not in x))

print(fnmatch.fnmatch('d1@gmail.h', '*?[0-9]*?.*?'))
print(fnmatch.filter(a, '*@*'))