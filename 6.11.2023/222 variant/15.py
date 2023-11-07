def f(a, b, x):
    if a <= x <= b:
        return True
    else:
        return False

mn=10**9

for a in range(0, 10000):
    for b in range(a, 10000):
        k=0
        for i in range(1, 200):
            x = i/2
            if ((f(254, 800, x) and (not f(a, b, x))) <= (f(410, 823, x))):
                k=k+1

        if k==199:
            mn=min(mn, b-a)
print(mn)