s = 125 ** 300 * 5 ** 300 - 25 ** 70 - 100
k = 0

while s > 0:
    b = s % 10
    if b == 4:
        k += 1
    s //= 10

print(k)