def f(x: int, y: int) -> int:
    if x == y:
        return 1
    if x > y:
        return 0

    return f(x + 1, y) + f(x + 5, y) + f(x * 3, y)

print(f(3, 9) * f(9, 15) * f(15, 24))