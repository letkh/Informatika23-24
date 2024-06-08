import math


def find_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


for n in range(26_600, 28_100):
    k = len(find_divisors(n)) - 2
    if k % 13 == 0 and k != 0:
        print(n, k)
