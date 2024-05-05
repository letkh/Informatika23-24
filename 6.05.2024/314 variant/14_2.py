import string
n = string.digits + string.ascii_uppercase[:17]
for x in n:
    a = int(f'123{x}24', 27)
    b = int(f'{x}178', 27)
    if (a + b) % 26 == 0:
        print((a + b) // 26)