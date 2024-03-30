from turtle import *
tracer(0)
k = 20
lt(90)
pd()
for i in range(2):
    fd(19 * k)
    rt(90)
    fd(10 * k)
    rt(90)
pu()
back(3 * k)
rt(90)
fd(8 * k)
lt(90)
pd()
for i in range(2):
    fd(32 * k)
    rt(90)
    fd(12 * k)
    rt(90)

pu()
for x in range(0 * k, 20 * k, k):
    for y in range(-10 * k, 30 * k, k):
        goto(x, y)
        dot(2, 'red')

done()