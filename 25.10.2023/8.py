def toNine(n):
    s = ''
    while n > 0:
        s = str(n % 9) + s
        n //= 9
    return s

def odd(n):
    n = int(n)
    k = 0
    while n > 0:
        if n % 2 != 0:
            k += 1
        n //= 10
    return k
k = 0
for i in range(10000000):
    if len(toNine(i)) == 7:
        n = toNine(i)
        if n.count('6') == 1 and odd(n) == 2:
            k += 1
    if len(toNine(i)) > 7:
        break
print(k)