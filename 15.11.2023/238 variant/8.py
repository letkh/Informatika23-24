nabor = 'КОМ'
k = 0
for x1 in nabor:
    for x2 in nabor:
        for x3 in nabor:
            for x4 in nabor:
                for x5 in nabor:
                    for x6 in nabor:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if (x4 != 'К' and x5 != 'К' and x6 != 'К') and (s.count('К') <= 2):
                            # print(s)
                            k += 1
print(k)
