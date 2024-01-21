def check(x):
    for d in range(19, x, 10):
        if x % d == 0:
            return d
    return False

for x in range(600001, 1000000):
    min_d = check(x)
    if min_d != 0:
        print(x, min_d)