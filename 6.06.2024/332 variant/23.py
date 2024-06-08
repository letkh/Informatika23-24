def f(x: int, y: int) -> int:
    if x == y: return 1
    if x > y: return 0

    return f(x + 2, y) + f(x + 5, y) + f(x ** 2, y)

print(f(12, 77) * f(77, 108))