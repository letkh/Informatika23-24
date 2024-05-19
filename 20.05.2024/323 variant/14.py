import string
n = string.digits + string.ascii_uppercase[:11]
for x in n:
    k = 0
    for y in n:
        a = int(f'12{y}{x}9',21)
        b = int(f'36{y}99',21)
        if (a + b) % 18 == 0:
            k += 1
    if k == 21:
        a = int(f'125{x}9', 21)
        b = int(f'36599', 21)
        print((a + b)//18)
        break
