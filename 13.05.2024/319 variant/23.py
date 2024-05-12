def f(x, y):
    if x == y:
        return 1
    if x > y or x == 22:
        return 0
    return f(x + 4, y) + f(x + 3, y)

print(f(10, 65))