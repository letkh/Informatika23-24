def f(x,y,a): 
    return (x**2 + y**2 > 128) or (y < -x + a)

for a in range(1000):
    if all(f(x,y,a) for x in range(10000) for y in range(10000)):
        print(a); break