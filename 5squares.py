import turtle
t = turtle.Turtle()

turtle.bgcolor("black")
turtle.title("5 squares")
t.pensize(5)
t.pencolor("skyblue")
t.speed(2)
for i in range(5):
    for j in range(4):
        t.lt(90)
        t.fd(100)
    t.lt(72)
    
turtle.done()

