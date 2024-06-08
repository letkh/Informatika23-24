from turtle import *
screensize(10_000, 10_000)
tracer(0)
k = 50
lt(90)
pd()
rt(120)
for i in range(3):
    rt(30)
    fd(6 * k)
    rt(30)
rt(30)
for i in range(3):
    fd(6 * k)
    rt(60)
pu()
for x in range(-10 * k, 10 * k, k):
    for y in range(-10 * k, 10 * k, k):
        goto(x, y)
        dot(3, 'red')
done()