nab = 'АЕИКЛПР'
k = 0
c = 0
for x1 in nab:
    for x2 in nab:
        for x3 in nab:
            for x4 in nab:
                for x5 in nab:
                    for x6 in nab:
                        k += 1
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if x1 != 'К' and s.count('И') >= 2 and k % 2 == 0:
                            c += 1
print(c)