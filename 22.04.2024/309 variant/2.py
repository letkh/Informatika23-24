print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x and (not ((not y) <= ((not w) and z))) and (not (z and y))):
                    print(x, y, z, w)