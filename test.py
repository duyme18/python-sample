import turtle

for angle in range(0, 360, 6):
    turtle.up()
    turtle.goto(0, 0)
    """
    turtle.seft()
    Phương thức này được sử dụng để thiết lập hướng của con rùa thành to_angle. 
    Phương thức này chỉ yêu cầu một đối số là một góc.
    """
    turtle.seth(90 - angle)
    print(angle)
    turtle.fd(120)
    turtle.down()
    turtle.fd(30)