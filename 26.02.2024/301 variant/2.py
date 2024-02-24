print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x == y) <= ((not z) or w)) == (not ((w <= x) or (y <= z)))) == 1:
                    print(x, y, z, w)