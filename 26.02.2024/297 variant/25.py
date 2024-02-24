def count_dividers(n):
    count = 0
    divider = 2
    while divider ** 2<n:
        if n % divider == 0:
            count += 2
        if count > 6:
            return count
        divider += 1
    if divider ** 2 == n:
        count += 1
    return count

c = 0
mn = 60000001
for i in range(50_000_000, 60_000_001):
    if i % 911 == 0:
        if count_dividers(i) == 6:
            c += 1
            mn = min(mn, i)

print(c, mn)