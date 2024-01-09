def f(x,y):
    if x == y:
        return 1
    if x < y or x == 4 or x == 43:
        return 0
    return f(x - 1, y) + f(x // 3, y) + f(int(x ** 0.5), y)

print(f(98,14) * f(14, 2))