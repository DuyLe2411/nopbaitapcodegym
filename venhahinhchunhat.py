import turtle



t = turtle.Turtle()
t.hideturtle()
t.pencolor('black')
t.pensize(3)
t.speed(0)
turtle.bgcolor("skyblue")

def Rectangular(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.fd(height)
    t.rt(90)
    t.fd(width)
    t.rt(90)
    t.fd(height)
    t.rt(90)
    t.fd(width)
    t.rt(90)
    t.end_fill()

t.penup()
t.goto(-200,0)
t.pendown()
Rectangular(t, 220, 100, "light green" )
turtle.bgcolor("black")

t.penup()
t.goto(-100,0)
t.pendown()
Rectangular(t, 220, 100, "light green")
turtle.bgcolor("skyblue")

t.penup()
t.goto(0,0)
t.pendown()
Rectangular(t, 220, 200 , "light green")
turtle.bgcolor("black")

t.penup()
t.goto(-200, 220)
t.pendown()
Rectangular(t, 220, 100, "light green")
turtle.bgcolor("skyblue")

t.penup()
t.goto(-100, 220)
t.pendown()
Rectangular(t, 220, 100, "light green")
turtle.bgcolor("black")
t.penup()
t.goto(-170,150)
t.pendown()
Rectangular(t, 80, 40, "white")
turtle.bgcolor("skyblue")

t.penup()
t.goto(-75,150)
t.pendown()
Rectangular(t, 80, 40, "white")
turtle.bgcolor("black")

t.penup()
t.goto(-170,-70)
t.pendown()
Rectangular(t, 80, 40, "white")
turtle.bgcolor("skyblue")
t.penup()
t.goto(-75,-70)
t.pendown()
Rectangular(t, 80, 40, "white")
turtle.bgcolor("black")

t.penup()
t.goto(60, -75)
t.pendown()
Rectangular(t, 145, 40, "dark blue" )
turtle.bgcolor("skyblue")
t.penup()
t.goto(100, -75)
t.pendown()
Rectangular(t, 145, 40, "dark blue")
turtle.done()