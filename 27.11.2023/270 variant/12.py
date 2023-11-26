def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a
a = []
print(is_prime(8))
for n in range(1, 1000):
    s = '>' + '0' * 31 + '1' * n + '2' * 47

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '21>', 1)
        if '>2' in s:
            s = s.replace('>2', '12>', 1)
        if '>0' in s:
            s = s.replace('>0', '2>', 1)
    b = int(s[:-1])
    sum = 0
    while b > 0:
        sum += b % 10
        b //= 10
    if is_prime(sum):
        a.append(n)

print(min(a))