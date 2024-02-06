nab = 'агилмноф'
k = 0
c = 0
for x1 in nab:
    for x2 in nab:
        for x3 in nab:
            for x4 in nab:
                for x5 in nab:
                    s = x1 + x2 + x3 + x4 + x5
                    k += 1
                    if x1 != 'н' and s.count('о') <= 1 and k % 2 != 0:
                        c += 1

print(c)