nab = 'ПРОСТ'
k = 0
for x1 in nab:
    for x2 in nab:
        for x3 in nab:
            for x4 in nab:
                for x5 in nab:
                    for x6 in nab:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if s.count('П') == 1 and s.count('Р') == 1 and s.count('С') == 1 and s.count('Т') == 1 and s.count('О') == 2 and 'ОО' not in s:
                            k += 1
print(k)
