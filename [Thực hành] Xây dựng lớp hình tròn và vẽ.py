import turtle
import math


class Circle:
    def __init__(self, r, x, y):
        """
        Hàm khởi tạo có tham số
        :param r: Bán kính
        :param x: Hoành độ x của tâm hình tròn
        :param y: Tung độ y của tâm hình tròn
        """
        self.r = r
        self.x = x
        self.y = y

    def draw(self):
        """Phương thức vẽ đường tròn"""
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.circle(self.r)
        turtle.done()

    def area(self):
        """Phương thức tính diện tích hình tròn"""
        return math.pi * self.r ** 2

    def perimeter(self):
        """
        Phương thức tính chu vi đường tròn
        """
        return 2 * math.pi * self.r


c = Circle(100, -200, 0)
c.draw()
print("S = ", c.area())
print("C = ", c.perimeter())
