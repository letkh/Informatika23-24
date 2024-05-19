import string
n = string.digits[1:7]
c = 0
for x1 in n:
    for x2 in n:
        for x3 in n:
            for x4 in n:
                for x5 in n:
                    s = x1 + x2 + x3 + x4 + x5
                    if s.count('1') == 1:
                        c += 1
print(c)