nab = 'АГЛОЬ'
k = 0
for x1 in nab:
    for x2 in nab:
        for x3 in nab:
            for x4 in nab:
                for x5 in nab:
                    k += 1
                    if (x1 + x2 + x3 + x4 + x5) == 'ОЛЬГА':
                        print(k)