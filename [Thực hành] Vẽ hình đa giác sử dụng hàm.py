import turtle

t = turtle.Turtle()

t.hideturtle()
t.pencolor('red')

def draw(n, w):
    for i in range(n):
        angle = (n - 2) * 180 / n
        t.fd(w)
        t.lt(180- angle)
    turtle.done()

draw(10, 100)