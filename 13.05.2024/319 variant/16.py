a = [0] * 3865
for n in range(0, 3865):
    if n < 4:
        a[n] = n
    if n > 3 and n % 2 != 0:
        a[n] = n * a[n - 1] + a[n - 2]
    if n > 3 and n % 2 == 0:
        a[n] = a[n - 2] + n // 2 - a[n - 4]

print(a[3858] + a[3864])
