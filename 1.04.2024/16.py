def f(n: int) -> int:
    if n == 1 or n == 2:
        return 3
    if n > 2:
        return 5 * f(n-1) - 4 * f(n-2)
print(f(15))