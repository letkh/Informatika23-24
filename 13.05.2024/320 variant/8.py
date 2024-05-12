import string
n = string.digits
def f(s):
    res = []
    for i in s:
        if s.count(i) == 2:
            res.append(i)
    if len(res) == 2:
        if f'{res[0]}{res[0]}' in s:
            return 1
    return 0
c = 0
for x1 in n[1:]:
    for x2 in n:
        for x3 in n:
            for x4 in n:
                s = x1 + x2 + x3 + x4
                if f(s) == 1:
                    c += 1
print(c)
