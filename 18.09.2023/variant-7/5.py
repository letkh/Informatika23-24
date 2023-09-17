def sum(a):
    s = 0
    n = int(a)
    while n:
        s += n % 10
        n //= 10
    return s

for n in range(10000):
    nOst = n - (n % 4)
    nInBin = format(nOst, 'b')
    s = str(nInBin) + str(sum(nInBin) % 2)
    s = str(s) + str(sum(int(s)) % 2)
    r = int(s, 2)
    if r < 64:
        print(n) # -> 15