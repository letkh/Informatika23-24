n = 'авзптхщя'
k = 0
c = 0
for x1 in n:
    for x2 in n:
        for x3 in n:
            for x4 in n:
                for x5 in n:
                    for x6 in n:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        c += 1
                        if c % 2 != 0 and x1 == 'т' and s.count('х') == 2:
                            k += 1
print(k)
