for x in range(10):
    o1 = int(f'1{x}234')
    o2 = int(f'1{x}243')
    a = 1 * o1 ** 2 + 1 * o1 ** 1 + 2
    b = 1 * o2 ** 2 + 1 * o2 ** 1 + 1
    if (a + b) % 15 == 0:
        print((a + b) / 15)