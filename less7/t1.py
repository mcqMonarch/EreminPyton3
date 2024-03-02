import random

x = [random.randint(-10, 10) for i in range(50)]
print(sorted(x, key=lambda s: (x.count(s), -s), reverse=True))
