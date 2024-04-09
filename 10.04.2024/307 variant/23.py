def f(x: int, y: int) -> int:
    if x == y:
        return 1
    if x < y or (x == 29 and x == 27):
        return 0
    return f(x // 4, y) + f(x - 1, y) + f(x - 2, y)

print(f(33,20))