def f(x, y):
    if x == y: return 1
    if x > y or x == 81: return 0

    return f(x + 3, y) + f(2 * x - 1, y) + f(x + int(str(x)[:1]), y)

print(f(42, 73) * f(73, 89))