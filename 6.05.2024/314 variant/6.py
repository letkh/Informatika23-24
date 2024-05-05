from turtle import *
tracer(0)
k = 20
lt(90)
pd()
for i in range(2):
    fd(13 * k)
    rt(90)
    fd(18 * k)
    rt(90)
pu()
fd(5 * k)
rt(90)
fd(9 * k)
lt(90)
pd()
for i in range(2):
    fd(11 * k)
    rt(90)
    fd(7 * k)
    rt(90)

pu()
for x in range(-30 * k, 30 * k, k):
    for y in range(-30 * k, 30 * k, k):
        goto(x, y)
        dot(2, 'red')
done()