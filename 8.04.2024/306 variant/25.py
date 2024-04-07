from fnmatch import fnmatch
import math


def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.extend([n])
    return list(set(divs))


for i in range(0, 10**6):
    if fnmatch(str(i), '12*567'):
        if sum(divisors(i)) % 12 == 0:
            print(i, sum(divisors(i)))
