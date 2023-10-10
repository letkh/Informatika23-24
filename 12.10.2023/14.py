x = 3 * 16 ** 8 - 4 ** 5 + 3
print(x)
k = 0

while x > 0:
    b = x % 4
    if (b == 3):
        k += 1
    x //= 4

print(k)