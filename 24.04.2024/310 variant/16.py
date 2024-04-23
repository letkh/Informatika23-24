def f(n):
    if n == 1:
        return 3
    if n % 2 == 0:
        return n + f(n/2)
    if n > 1 and n % 2 != 0:
        return 3 * f(n-1)

print(f(115))