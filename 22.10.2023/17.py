def f(n1, n2):
    if n1 > n2 or n1 == 17:
        return 0
    if n1 == n2:
        return 1

    return f(n1 + 1, n2) + f(n1 * 2, n2)

print(f(1, 10) * f(10, 21))