import  turtle as tur

tur.bgcolor("black")
pen = tur.Turtle()
pen.color('red')
pen.speed(15)

def draw_square():
    for side in range(4):
        pen.forward(100)
        pen.right(90)
pen.penup()
pen.back(20)
pen.pendown()

for sqaure in range(80):
    draw_square()
    pen.forward()
    pen.left(5)

pen.hideturtle()