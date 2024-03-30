def f(l, r, x):
    return l <= x <= r


mn = 10 ** 9
for a in range(0, 100):
    for b in range(a, 100):
        k=0
        for i in range(1, 200):
            x = i/2
            if (f(47, 115, x) <= (((not f(a, b, x) and (f(24, 90, x)))) <= (not f(47, 115, x)))):
                k=k+1

        if k==199:
            mn=min(mn, b-a)
print(mn)