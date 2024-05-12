import string
n = string.digits + string.ascii_uppercase[:6]
c = 0
for x1 in n[1:]:
    for x2 in n:
        for x3 in n:
            for x4 in n:
                for x5 in n:
                    s = x1 + x2 + x3 + x4 + x5
                    if s.count('7') <= 1 and not any(int(s[x], 16) % 2 == 1 and int(s[x + 1], 16) % 2 == 1 for x in range(len(s) - 1)):
                        c += 1
print(c)