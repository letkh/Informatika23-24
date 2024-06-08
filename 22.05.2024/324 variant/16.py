def f(n: int) -> int:
    if n <= 30:
        return 3
    if 30 < n <= 250:
        return -3 + 2 * f(n - 29)
    if 250 < n <= 900:
        return 2 + f(n - 43)
    if n > 900:
        return 3 + f(n - 62)

print(f(1400))