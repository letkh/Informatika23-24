nab = 'АГДИЛНРЯ'
k = 0
for x1 in nab:
    for x2 in nab:
        for x3 in nab:
            for x4 in nab:
                for x5 in nab:
                    for x6 in nab:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        k += 1
                        if k % 2 == 0 and x1 != 'Я' and s.count('Д') == 3:
                            print(k)