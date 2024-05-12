from turtle import *
lt(90)
tracer(0)
k = 20
pd()
for i in range(6):
    rt(90)
    fd(1 * k)
    rt(90)
    fd(11 * k)
pu()
fd(3 * k)
rt(90)
fd(5 * k)
pd()
for i in range(10):
    fd(12 * k)
    rt(90)
pu()
for x in range(-20 * k, 20 * k, k):
    for y in range(-20 * k, 20 * k, k):
        goto(x, y)
        dot(2, 'red')
done()