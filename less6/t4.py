p1 = '  d fg      r'.lower().replace(' ', '')
p2 = 'fg rd     '.lower().replace(' ', '')
p1 = sorted(p1)
p2 = sorted(p2)
print(p1 == p2)