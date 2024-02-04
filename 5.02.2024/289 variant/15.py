p = [2,4,6,8,10,12,14,16,18,20]
q = [3,6,9,12,15,18,21,24,27,30]

for g1 in range(1, 100):
    for g2 in range(g1, 100):
        a = list(range(g1,g2))
        if all(((x in a) <= (x in p)) and ((not x in q) <= (not x in a)) for x in range(1000)):
            if str(a) != '[]':
                print(a)