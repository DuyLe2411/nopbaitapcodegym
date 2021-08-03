import turtle

t = turtle.Turtle()
t.fillcolor("yellow")
t.begin_fill()
turtle.bgcolor("blue")
t.pensize(10)
t.pencolor("red")
t.speed(1)
t.shapesize(4,4,4)


t.fd(200)
t.rt(90)
turtle.bgcolor("white")
t.pencolor("brown")

t.fd(100)
t.rt(90)
turtle.bgcolor("black")

t.fd(200)
t.rt(90)
turtle.bgcolor("pink")

t.fd(100)
t.rt(90)
turtle.bgcolor("purple")

t.end_fill()

turtle.done()