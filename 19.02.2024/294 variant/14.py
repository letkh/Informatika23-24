a = 2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338
c = 0
while a > 0:
    if a % 9 != 0:
        c += 1
    a //= 9

print(c)