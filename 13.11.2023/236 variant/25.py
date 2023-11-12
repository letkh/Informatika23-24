def F(n):
    divisors = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    if divisors:
        return max(divisors) - min(divisors)
    else:
        return 0

c = 0
i = 850001
while c < 6:
    m = F(i)
    if m and m % 7 == 0:
        print(i, m)
        c += 1
    i += 1