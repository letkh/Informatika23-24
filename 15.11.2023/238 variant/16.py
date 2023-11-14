def f(n):
    if n < 20:
        return 2
    if 20 <= n < 150:
        return 1 + 2 * f(n - 17)
    if 150 <= n < 1000:
        return -3 + f(n-23)
    if n >= 1000:
        return 2 + f(n-42)
print(f(1150))