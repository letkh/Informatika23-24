print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( (x == y) and (w <= z) ) == 0:
                    print(x, y, z,w)
print()
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( (x <= y) <= (w == z) ) == 0:
                    print(x, y, z,w)