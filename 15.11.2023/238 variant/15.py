def f(a, b):
    divisors = [i for i in range(1, min(a, b) + 1) if not (a % i or b % i)]
    return len(divisors) == 1

for a in range(1, 10000):
    k = 0
    for x in range(200):
        if ( (f(x, 360) <= f(x, a)) and (f(x, a) <= f(x, 240)) ):
            k += 1
        if k == 200:
            print(a)