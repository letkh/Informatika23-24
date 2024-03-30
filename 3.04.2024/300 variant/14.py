for x in '0123456789ABCDEFGHI':
    a = int(f'5{x}642535', 19)
    b = int(f'78{x}11114', 19)
    c = int(f'9334{x}39', 19)
    if (a + b + c) % 18 == 0:
        print((a + b + c) // 18)