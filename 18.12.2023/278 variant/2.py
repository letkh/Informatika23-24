print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( (x <= z) and (w and ((not (y)) == z)) ):
                    print(x, y, z,w) 