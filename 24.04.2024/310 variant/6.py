from turtle import *
tracer(0)
lt(90)
pd()
rt(90)
k = 50
for i in range(8):
    fd(4 * k)
    lt(72)
pu()
for x in range(-10 * k, 10 * k, k):
    for y in range(-10 * k, 10 * k, k):
        goto(x, y)
        dot(2, 'RED')

done()