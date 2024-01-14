def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n//10) + n % 10
    if n % 2 != 0:
        return f(n//10)
print(f(1234))
# print(6 ** 9)