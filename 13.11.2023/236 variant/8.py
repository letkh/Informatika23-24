def toQuad(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return int(s)

def rightOrder(n):
    a = []
    while n > 0:
        a.append(n % 10)
        n //= 10
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            return False
    return True

k = 0

for i in range(100, 1000):
    if rightOrder(toQuad(i)) != True:
        continue
    k += 1
print(k)
    