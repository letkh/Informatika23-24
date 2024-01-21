import sys

sys.set_int_max_str_digits(50000000)
for x in range(0, 1000):
    c = 0
    a = 4 * 625 ** 1920 + 4 * 125 ** x - 4 * 25 ** 1940 - 3 * 5 ** 1950 - 1960
    while a > 0:
        if a % 5 == 0:
            c += 1
        a //= 5
    if c == 1891:
        print(x)
        break
