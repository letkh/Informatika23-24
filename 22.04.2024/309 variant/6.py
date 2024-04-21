from turtle import *
tracer(0)
lt(90)
k = 20
for i in range(2):
    fd(8*k)
    rt(90)
    fd(20*k)
    rt(90)
pu()
back(-3*k)
rt(90)
fd(5*k)
lt(90)
pd()
for i in range(2):
    fd(9*k)
    rt(90)
    fd(6*k)
    rt(90)
pu()
for x in range(-20 * k, 20 * k, k):
    for y in range(-20 * k, 20 * k, k):
        goto(x, y)
        dot(2, 'red')
done()