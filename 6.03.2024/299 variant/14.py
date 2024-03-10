import sympy

for x in '0123456789AB':
    for y in '0123456789ABCDEFGHI':
        a = int(f'5{x}9{x}4', 12)
        b = int(f'7{x}{x}6', 14)
        c = int(f'55{x}{x}8', 16)
        d = int(f'3{y}{x}7', 19)
        n = a + b + c - d
        if sympy.isprime(n):
            print(int(x, 12) * int(y, 19))
