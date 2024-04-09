import string

a = string.ascii_uppercase[10]

for x in '123456789' + a:
    a = int(f'183{x}89957', 22)
    b = int(f'80{x}33', 22)
    c = int(f'521{x}6', 22)
    if (a - b - c) % 21 == 0:
        print((a - b - c) // 21)