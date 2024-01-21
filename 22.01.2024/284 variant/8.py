digits = '012345678'
digit = '12345678'
c = 0
for x1 in digit:
    for x2 in digits:
        for x3 in digits:
            for x4 in digits:
                for x5 in digits:
                    s = x1 + x2 + x3 + x4 + x5
                    if s.count('3') == 1 and '35' not in s and '36' not in s and '37' not in s and '38' not in s and '53' not in s and '63' not in s and '73' not in s and '83' not in s:
                        c += 1
print(c)
