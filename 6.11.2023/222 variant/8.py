let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = 0
for x1 in let:
    for x2 in let:
        for x3 in let:
            for x4 in let:
                for x5 in let:
                    s = x1 + x2 + x3 + x4 + x5
                    for l in s:
                        if l in 'AEOIUY':
                            count += 1
print(count)