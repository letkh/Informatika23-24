a = 25 ** 9 + 5 ** 21 - 625
k = 0
while a > 0:
    if a % 5 == 4:
        k += 1
    a //= 5
print(k)