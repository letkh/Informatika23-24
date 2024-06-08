def vzp(a, b):
    return a if b == 0 else vzp(b, a % b)


for a in range(1, 1000):
    if all( ((vzp(x, 756) > 1) <= (vzp(x, a) > 1)) and ((vzp(x, a) > 1) <= (vzp(x, 756) > 1)) for x in range(1, 1000)):
        print(a)
        break