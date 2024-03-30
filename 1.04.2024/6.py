from turtle import *
tracer(0)
k = 25
lt(90)
pd()
for i in range(14):
    rt(60)
    fd(2 * k)
    rt(60)
    fd(2 * k)
    rt(270)
pu()
for x in range(-10 * k, 20 * k, k):
    for y in range(-20 * k, 30 * k, k):
        goto(x, y)
        dot(2, 'red')

done()