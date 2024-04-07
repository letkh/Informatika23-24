def f(n: int) -> int:
    if n >= 4264:
        return n + 4
    else:
        return n - 4 + f(n + 6)


print(f(4256) - f(4258))