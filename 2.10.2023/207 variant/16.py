def f(n):
    if n <= 1:
        return 1;
    if n == 2:
        return 2;
    if (n > 2) and (n % 4 == 0):
        return n - f(n // 4) - f(n - 3);
    if (n > 2) and (n % 4 != 0):
        return 2 + f(n - 1) + f(n // 5);

c = 0;
for x in range(40, 121):
    if (f(x) <= 240) and (f(x) > 60):
        c += 1;
print(c)