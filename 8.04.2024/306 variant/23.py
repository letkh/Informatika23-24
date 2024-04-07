def f(x: int, y: int) -> int:
    if x == y:
        return 1
    if x < y:
        return 0

    return f(x - 5, y) + f(x // 3, y) + f(x - 4, y)

print(f(43, 14))