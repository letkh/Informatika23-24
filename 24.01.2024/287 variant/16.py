def F(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n % 3 == 0:
        return 2 * n - F(n - 1) - F(n // 3)
    else:
        return n + F(n - 2) + F(n // 10)
count = 0
for i in range(50, 101):
    f = F(i)
    if f > 50 and f <= 200:
        count += 1
print(count)