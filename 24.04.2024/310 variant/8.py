import string

def f(s):
    s1, s2 = 0, 0
    for i in s:
        if int(i) % 2 == 0:
            s1 += 1
        else:
            s2 += 1
    return [s1, s2]
n = string.digits
c = 0
for x1 in n[1:]:
    for x2 in n:
        for x3 in n:
            for x4 in n:
                for x5 in n:
                    for x6 in n:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if len(set(list(s))) == len(list(s)) and x5 + x6 == '26' and (f(s)[1] == 2 or f(s)[0] == 3):
                            c += 1
print(c)