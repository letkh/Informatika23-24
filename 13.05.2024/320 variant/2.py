print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( ((w == (not y) or (w == (not z)))) and x and (y <= z) ):
                    print(x, y, z, w)