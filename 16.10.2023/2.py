a = 9 ** 7 + 3 ** 21 - 8
k = 0
while a > 0:
    k += a % 3
    a //= 3

print(k)