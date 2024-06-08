import math
def find_divisors(n):
    divisors = []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

for i in range(650_001, 700_000):
    if find_divisors(i) != []:
        if (max(find_divisors(i)) - min(find_divisors(i))) != 0 and (max(find_divisors(i)) - min(find_divisors(i))) % 279 == 0:
            print(i, (max(find_divisors(i)) - min(find_divisors(i))) // 279)