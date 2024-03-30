a = 9 ** 18 + 3 ** 54 - 9
c = 0
while a > 0:
    if a % 3 == 2:
        c += 1
    a //= 3
print(c)