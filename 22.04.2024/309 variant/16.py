def f(n: int) -> int:
    if n >= 3650:
        return n + 3
    else:
        return f(n + 4) * n

print(f(3641) - f(3644))