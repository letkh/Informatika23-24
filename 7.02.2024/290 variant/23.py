def f(x, y):
    if x == y: return 1
    if x > y or x == 6 or x == 17: return 0
    return f(x + 2, y) + f(x + 3, y) + f(x * 5, y)


print(f(1, 31))