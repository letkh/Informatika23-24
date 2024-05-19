from turtle import *
tracer(0)
k = 30
lt(90)
rt(180)
fd(2 * k)
rt(90)
fd(80 * k)
rt(90)
fd(2 * k)
for i in range(8):
    rt(180)
    circle(5 * k, -180)
up()

for x in range(-50 * k, 20 * k, k):
    for y in range(-50 * k, 20 * k, k):
        goto(x, y)
        dot(2,'red')

done()

print(48 * 8 + 7)