a = []
for n in range(4, 1000):
    s = '9' + '8' * 3
    while '98' in s or '888' in s or '7788' in s:
        if '98' in s:
            s = s.replace('98', '7', 1)
        if '888' in s:
            s = s.replace('888', '78', 1)
        if '7788' in s:
            s = s.replace('7788', '897', 1)
    if sum(map(int, s)) <= 399:
        a.append(n)
print(len(a))