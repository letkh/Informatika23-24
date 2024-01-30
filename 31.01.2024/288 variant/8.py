nab = 'АЕКПТЧ'
k = 0
a = 0
b = 0
for x1 in nab:
    for x2 in nab:
        for x3 in nab:
            for x4 in nab:
                for x5 in nab:
                    for x6 in nab:
                        for x7 in nab:
                            s = x1 + x2 + x3 + x4 + x5 + x6 + x7
                            k += 1
                            if s == 'АПТЕЧКА':
                                a = k
                            if s == 'ПЕЧАТКА':
                                b = k
print(a - b - 1)