import turtle


k = 30
turtle.speed(10000)
for i in range(6):
    turtle.forward(10 * k)
    turtle.right(90)

turtle.forward(2 * k)
turtle.right(90)

for i in range(2):
    turtle.forward(15 * k)
    turtle.right(90)
    turtle.forward(4 * k)
    turtle.right(90)

turtle.up()

for x in range(0, 15 * k, k):
    for y in range(-10 * k, 8 * k, k):
        turtle.goto(x, y)
        turtle.dot(3, 'red')

turtle.done()