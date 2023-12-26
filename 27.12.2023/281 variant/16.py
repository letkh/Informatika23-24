def f(n):
    if n >= 2000:
        return 2000
    if n < 2000 and n % 2 != 0:
        return n * f(n + 1)
    if n < 2000 and n % 2 == 0:
        return n * f(n + 1) / 2
print(f(1998)/f(2001))