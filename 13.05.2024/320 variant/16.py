def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return n * (n - 1) * f(n - 1)

print(f(123) / f(120))

