import turtle

pen = turtle.Turtle()

pen.hideturtle()
pen.pencolor('red')

def goto(x,y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

def draw_house(w, h):
    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(w)
        pen.right(90)
        pen.fd(h)
        pen.right(90)
    pen.end_fill()


goto(0,0)
draw_house(100, 200)
goto(-200,0)
draw_house(100, 200)
turtle.done()