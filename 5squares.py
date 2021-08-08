

import turtle
t = turtle.Turtle()

turtle.bgcolor("black")
turtle.title("5 squares")
t.pensize(5)
t.pencolor("skyblue")
t.speed(2)
for i in range(5):
    t.lt(100)
    for j in range(4):
        t.lt(90)
        t.fd(200)
        
    t.lt(188)
    
turtle.done()


