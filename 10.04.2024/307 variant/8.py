n = 'гжсцэ'
k = 0
for x1 in n:
    for x2 in n:
        for x3 in n:
            for x4 in n:
                for x5 in n:
                    for x6 in n:
                        k += 1
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if x1 != 'г' and x6 != 'г' and 'сс' not in s and k % 2 == 0:
                            print(k)
