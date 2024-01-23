for x in range(1, 13):
    a = int(f'186{x}4', 13)
    b = int(f'5{x}716', 13)
    if (a + b) % 11 == 0:
        print((a + b) / 11)