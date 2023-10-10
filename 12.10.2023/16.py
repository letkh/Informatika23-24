def f(n):
    if n <= 13:
        return n*n*n + n*n + 1
    if n > 13 and n % 3 == 0:
        return f(n-1) + 2*n*n - 3
    if n > 13 and n % 3 != 0:
        return f(n-2) + 3*n + 6
k = 0

for n in range(1, 1001):
    if f(n) % 2 != 0:
        k += 1
print(k)