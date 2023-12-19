a = 8 ** 16 + 2 ** 52 - 15
k = 0
while a > 0:
    if a % 2 == 1:
        k += 1
    a //= 2
print(k)