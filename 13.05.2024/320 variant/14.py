import string
n = string.digits + string.ascii_uppercase[:7]
for x in n:
    if (int(f'135{x}9', 17) + int(f'9{x}531', 17)) % 9 == 0:
        print((int(f'135{x}9', 17) + int(f'9{x}531', 17)) // 9)
