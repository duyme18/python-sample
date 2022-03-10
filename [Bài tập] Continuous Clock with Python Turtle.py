import turtle
import datetime
import math

screen = turtle.Screen()
screen.title('Continuous Clock - CodeGym Online - Python')
screen.bgcolor('sky blue')
screen.setup(700, 700)
screen.setworldcoordinates(-700, -700, 700, 700)
screen.tracer(0, 0)


class clock:
    def __init__(self, hour, minute, second):
        self.hour, self.minute, self.second = hour, minute, second
        self.microsecond = 0
        self.face = turtle.Turtle()
        self.hand = turtle.Turtle()
        self.face.hideturtle()
        self.hand.hideturtle()

    def draw(self):
        self.draw_face()
        self.draw_hand()

    def draw_face(self):
        self.face.clear()
        self.face.up()
        self.face.goto(0, -500)
        self.face.pensize(4)
        self.face.down()
        self.face.fillcolor('white')
        self.face.begin_fill()
        """
        radius: Radius of the circle.
        extent: The part of the circle in degrees as an arc.
        steps: Divide the shape in the equal number of given steps.
        """
        self.face.circle(500, steps=100)
        self.face.end_fill()
        self.face.up()
        self.face.goto(0, 0)
        self.face.dot(10)

        # vẽ vạch phút
        self.face.pensize(2)
        for angle in range(0, 360, 6):
            self.face.up()
            self.face.goto(0, 0)
            """
            turtle.seft()
            Phương thức này được sử dụng để thiết lập hướng của con rùa thành to_angle. 
            Phương thức này chỉ yêu cầu một đối số là một góc.
            """
            self.face.seth(90 - angle)
            self.face.fd(420)
            self.face.down()
            self.face.fd(30)

        # vẽ vạch giờ
        self.face.pensize(3)
        for angle in range(0, 360, 30):
            self.face.up()
            self.face.goto(0, 0)
            self.face.seth(90 - angle)
            self.face.fd(400)
            self.face.down()
            self.face.fd(50)

        # vẽ vạch 12h, 3h, 6h, 9h
        self.face.pensize(4)
        for angle in range(0, 360, 90):
            self.face.up()
            self.face.goto(0, 0)
            self.face.seth(90 - angle)
            self.face.fd(380)
            self.face.down()
            self.face.fd(70)

    def draw_hand(self):
        # vẽ kim giờ
        self.hand.clear()
        self.hand.up()
        self.hand.goto(0, 0)
        self.hand.seth(90 - math.floor(((
                                                self.hour % 12) * 60 * 60 * 1000000 + self.minute * 60 * 1000000 + self.second * 1000000 + self.microsecond) / 3600000000 * 30))
        self.hand.down()
        self.hand.color('black')
        self.hand.pensize(6)
        self.hand.fd(230)

        # vẽ kim phút
        self.hand.up()
        self.hand.goto(0, 0)
        self.hand.seth(
            90 - math.floor((self.minute * 60 * 1000000 + self.second * 1000000 + self.microsecond) / 60000000 * 6))
        self.hand.down()
        self.hand.color('black')
        self.hand.pensize(4)
        self.hand.fd(300)

        # vẽ kim giây
        self.hand.up()
        self.hand.color('red')
        self.hand.goto(0, 0)
        self.hand.dot(5)
        self.hand.seth(90 - (self.second * 1000000 + self.microsecond) / 1000000 * 6)
        self.hand.down()
        self.hand.pensize(2)
        self.hand.fd(350)


def animate():
    global c
    d = datetime.datetime.now()
    c.hour, c.minute, c.second, c.microsecond = d.hour, d.minute, d.second, d.microsecond
    c.draw_hand()
    screen.update()
    screen.ontimer(animate, 100)


d = datetime.datetime.now()
c = clock(d.hour, d.minute, d.second)
c.draw_face()
screen.update()
animate()
turtle.done()
