def f(x, y, a):
    return (3*x + y > a) and (y < x) and (x < 30)

b = []
for a in range(1, 1000):
    if all(f(x, y, a) == 0 for x in range(100) for y in range(100)):
        b.append(a)

print(min(b))