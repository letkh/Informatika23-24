n = 'агклопру'
k = 0
c = 0
for x1 in n:
    for x2 in n:
        for x3 in n:
            for x4 in n:
                for x5 in n:
                    s = x1 + x2 + x3 + x4 + x5
                    k += 1
                    if k % 2 == 0 and x1 != 'г' and s.count('л') <= 2:
                        c += 1
print(c)
