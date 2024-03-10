import turtle as t

k = 20
t.left(40)
t.speed(10000)
for i in range(5):
    t.right(-95)
    t.forward(12 * k)
    t.left(45)
    t.forward(8 * k)
    t.left(40)

t.up()

for x in range(-20 * k, 10 * k, k):
    for y in range(-10 * k, 10 * k, k):
        t.goto(x, y)
        t.dot(3, 'red')

t.done()