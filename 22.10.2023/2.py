print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ( (( (not x) or z) == (y and (not w))) <= (z and y) ) == 0:
                    print(x,y,z,w)