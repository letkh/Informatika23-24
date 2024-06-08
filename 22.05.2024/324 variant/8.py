n = 'сон'
c = 0
for x1 in n:
    for x2 in n:
        for x3 in n:
            for x4 in n[1:]:
                for x5 in n[1:]:
                    for x6 in n[1:]:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if s.count('с') == 1 or s.count('с') == 3 or s.count('с') == 0:
                            c += 1
print(c)