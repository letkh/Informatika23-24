n = 'амосшщэ'
c = 0
for x1 in n:
    for x2 in n:
        for x3 in n:
            for x4 in n:
                c += 1
                if x1 == 'с' and x4 == 'э':
                    print(c)