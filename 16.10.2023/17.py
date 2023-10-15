sum = 0
for x in range(1, 10):
    a = (27 ** 7) - (3 ** 11) + 36 - x
    sum = 0
    while a > 0:
        sum += a % 3
        a //= 3
    if sum == 22:
        print(x)