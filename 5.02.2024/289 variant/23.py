def f(x, y):
    if x == y:return 1
    if x == 11 or x == 12 or x > y: return 0

    return f(x + 1, y) + f(x * 2, y) + f(x **2, y)

print(f(2, 10) * f(10, 40))