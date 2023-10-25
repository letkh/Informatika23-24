max = 0
for i in range(200, 1000):
    s = '1' * i
    while ('1111' in s):
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    if max < s.count('1'):
        max = s.count('1')
        index = i
print(index)