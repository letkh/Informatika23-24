n = '012345'
c = 0
for x1 in n[1:]:
    for x2 in n:
        for x3 in n:
            for x4 in n:
                s = x1 + x2 + x3 + x4
                if s.count('4') == 0 and len(list(set(list(s)))) == len(list(s)) and int(x1) % 2 != int(x2) % 2 and int(x2) % 2 != int(x3) % 2 and int(x3) % 2 != int(x4) % 2:
                    c += 1
print(c)