nab = 'екоф'
k = 0
a = []
for x1 in nab:
    for x2 in nab:
        for x3 in nab:
            for x4 in nab:
                for x5 in nab:
                    s = x1 + x2 + x3 + x4 + x5
                    k += 1
                    if s.count('о') == 1 and 'ко' not in s and 'ок' not in s and 'фо' not in s and 'оф' not in s:
                        a.append(k)

print(a[0] + a[-1])