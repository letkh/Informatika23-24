nab = 'СТЕПАН'
let = ['С', 'Т', 'П', 'Н']
k = 0
c = 0
for x1 in nab:
    for x2 in nab:
        for x3 in nab:
            for x4 in nab:
                s = x1 + x2 + x3 + x4
                k = 0
                for i in range(len(s)):
                    if s[i] in let:
                        k += 1
                if k == 2:
                    c += 1
print(c)