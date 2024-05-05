n = 'апрсу'
k = 0
a = []
for x1 in n:
    for x2 in n:
        for x3 in n:
            for x4 in n:
                for x5 in n:
                    s = x1 + x2 + x3 + x4 + x5
                    k += 1
                    if 'аа' not in s and s.count('у') <= 1:
                        a.append(k)
print(min(a))