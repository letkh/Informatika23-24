b = []
for x in range(1, 37):
    for y in range(1, 37):
        a = 2 * 37 ** 7 + 1 * 37 ** 6 + x * 37 ** 5 + 4 * 37 ** 4 + 5 * 37 ** 3 + 7 * 37 ** 2 + y * 37 + 9
        if a % 36 == 0:
            t = y * 37 + x
            b.append(int(t))
print(max(b))