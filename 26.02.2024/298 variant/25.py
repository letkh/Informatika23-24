def count_dividers(n):
    count = 0
    divider = 2
    max_divider = 0
    while divider ** 2<n:
        if n % divider == 0:
            count += 2
            max_divider = max(max_divider, n // divider, divider)
        if count > 6:
            return count, max_divider
        divider += 1
    if divider ** 2 == n:
        max_divider = max(max_divider, n // divider, divider)
        count += 1
    return count, max_divider

c = 0
md = 0
for i in range(50_000_000, 60_000_001):
    if i % 911 == 0:
        if count_dividers(i)[0] == 6:
            c += 1
            md = max(md, count_dividers(i)[1])

print(c, md)