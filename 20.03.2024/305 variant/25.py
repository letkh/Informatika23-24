n = 860001
c = 0

while c != 5:
    for i in range(2, n):
        if n % i == 0:
            M = n // i - i
            break
    if M % 100 == 30:
        c += 1
        print(n, M)
    n += 1