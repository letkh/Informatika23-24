from turtle import *
tracer(0)
k = 15
lt(90)
for i in range(12):
    goto(xcor() + 3 * k, ycor() + 3 * k)
    goto(xcor() - 8 * k, ycor() + 2 * k)
    goto(xcor() + 5 * k, ycor() - 5 * k)
up()
for x in range(-40 * k, 40 * k, k):
    for y in range(-40 * k, 40 * k, k):
        goto(x, y)
        dot(2, 'red')
done()