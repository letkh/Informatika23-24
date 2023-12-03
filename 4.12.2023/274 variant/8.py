nabor = 'АВИОРТФ'
k = 0
c = 0
for x1 in nabor:
    for x2 in nabor:
        for x3 in nabor:
            for x4 in nabor:
                for x5 in nabor:
                    for x6 in nabor:
                        k += 1
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if k % 2 == 0 and x1 != 'О' and s.count('Р') == 2:
                            c += 1
print(c)
