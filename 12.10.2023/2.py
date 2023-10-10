print('x y z')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0,2):
            if ((not x) and y and z) or ((not x) and (not z)) == 1:
                print(x,y,z)