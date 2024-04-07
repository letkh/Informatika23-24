from turtle import *
tracer(0)
k = 15
lt(90)
pd()
rt(45)
for i in range(7):
    fd(7 * k)
    rt(45)
    fd(20 * k)
    rt(135)
pu()
for x in range(-10 * k, 30 * k, k):
    for y in range(-20 * k, 30 * k, k):
        goto(x, y)
        dot(2, 'red')

done()