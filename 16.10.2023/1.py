a = 9 ** 9 + 3 ** 21 - 7
k = 0
while a > 0:
    if (a % 3 == 0):
        k += 1
    a //= 3

print(k)