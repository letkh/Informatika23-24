print([int(f'451{x}', 18) + int(f'79{x}2', 18) for x in '123456789ABCDEFGH' if (int(f'451{x}', 18) + int(f'79{x}2', 18)) % 27 == 0][0] // 27)