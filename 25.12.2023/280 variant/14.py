for x in range(1, 23):
    a = int(f'2{x}{x}341011', 23)
    b = int(f'220{x}4', 23)
    c = int(f'110{x}6', 23)
    if (a + b + c) % 22 == 0:
        print((a + b + c) / 22)