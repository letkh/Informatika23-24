from turtle import *
tracer(0)
k = 30
lt(90)
pd()
rt(270)
for i in range(2):
    fd(8 * k)
    rt(120)
rt(120)
for i in range(2):
    rt(120)
    fd(3 * k)
    rt(240)
rt(240)
for i in range(2):
    fd(14 * k)
    rt(120)

pu()
for x in range(-10 * k, 30 * k, k):
    for y in range(-20 * k, 30 * k, k):
        goto(x, y)
        dot(2, 'red')

done()