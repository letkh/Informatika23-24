def tr(n):
    s = ''
    while n > 0:
        s = str(n%3) + s
        n //= 3
    return s
def dig_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
def f(n):
    n2 = tr(n)
    s = ''
    if n % 2 == 0:
        s = f'1{n2}00'
    else:
        sum = dig_sum(int(n2))
        s = f'{n2}{tr(sum)}'
    return int(s, 3)

for n in range(100):
    if f(n) > 168:
        print(n)