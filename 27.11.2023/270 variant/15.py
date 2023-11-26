
b = []
for a in range(1, 10000):
    k = 0
    for x in range(0, 200):
        if ( x & 56 == 0 or (x & a != 0 or x & 35 == 0) ) == 1:
            k += 1
    if k == 200:
        b.append(a)
print(min(b))