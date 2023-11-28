l = []
for a in range(10000):
    k = 0
    for x in range(200):
        if ( (not ( x & 45 != 0 and x & a == 0)) or x & 33 != 0):
            k += 1
        if k == 200:
            l.append(a)
print(min(l))