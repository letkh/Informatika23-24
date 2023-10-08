k = 0
min = 1000;
for a in 'КНОРСЯ':
    for b in 'КНОРСЯ':
        for c in 'КНОРСЯ':
            for d in 'КНОРСЯ':
                for e in 'КНОРСЯ':
                    for f in 'КНОРСЯ':
                        s = a+b+c+d+e+f
                        k += 1;
                        if (k == 288):
                            print(s)
                        if s.count('К') < 3 and s.count('К') > 0 and s.count('Я') == 2:
                            if (k < min):
                                min = k;
print(min)