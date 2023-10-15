a = 81 ** 2017 + 9 ** 5223 - 81
k = 0
while a > 0:
    if a % 9 == 8:
        k += 1
    a //= 9
print(k)