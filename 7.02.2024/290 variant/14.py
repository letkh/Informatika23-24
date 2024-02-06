g = '0123456789ABCDEFGHIJKLMN'
for x in g:
    a = int(f'1{x}2{x}3{x}4{x}5', 25)
    b = int(f'2{x}024', 25)
    c = int(f'1{x}099', 25)
    if (a + b + c) % 24 == 0:
        print((a + b + c) // 24)