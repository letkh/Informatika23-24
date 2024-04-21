import string
n = string.digits[1:] + string.ascii_uppercase[:9]
for x in n:
    a = int(f'78{x}79643', 19)
    b = int(f'25{x}43', 19)
    c = int(f'63{x}5', 19)
    if (a + b + c) % 18 == 0:
        print((a + b + c) // 18)