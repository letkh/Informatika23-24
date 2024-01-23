nab = 'ЕКОР'
k = 0
a = []
for x1 in nab:
    for x2 in nab:
        for x3 in nab:
            for x4 in nab:
                for x5 in nab:
                    for x6 in nab:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        k += 1
                        if x1 == 'О' and 'ЕЕ' not in s:
                            a.append(k)
print(min(a))