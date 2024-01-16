from fnmatch import *

def f(x):
    count = 0
    sum_d = 0
    for d in range(1, x + 1):
        if x % d == 0:
            if d % 2 == 0:
                count += 1
                sum_d += d
    return count, sum_d

for x in range(65000, 10 ** 8 + 1, 1):
    if fnmatch(str(x), '6*97*5?'):
        count_d, sum_d = f(x)
        if count_d >= 4:
            print(x, sum_d)