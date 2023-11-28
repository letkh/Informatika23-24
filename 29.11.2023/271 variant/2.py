print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ( (y and x) or (y and (not z)) ):
                print(x,y,z)