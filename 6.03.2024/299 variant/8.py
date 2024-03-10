n = 'вася'
a = []
for x1 in n:
    for x2 in n:
        for x3 in n:
            for x4 in n:
                for x5 in n:
                    s = x1 + x2 + x3 + x4 + x5
                    if s.count('а') >= 1:
                        a.append(s)

print(len(a))