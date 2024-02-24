symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for p in (9, 36):
    for x in symbols[:p]:
        for y in symbols[:p]:
            for z in symbols[:p]:
                for w in symbols[1:int(p)]:
                    a = int(f'{z}{x}{y}{x}4', p)
                    b = int(f'{x}{y}658', p)
                    c = int(f'{w}{z}{x}73', p)
                    if (a + b) == c:
                        print(int(f'{x}{y}{z}{w}', int(p)))