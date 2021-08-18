distance = int(input("Nhập khoảng cách từ điểm bất kỳ đến tâm (0;0): "))

import turtle #import the turtle package and set colours and screen
import math as m

t = turtle.Turtle()
t.pensize(5)
turtle.bgcolor("black")
t.speed(0)
t.pencolor("yellow")
turtle.setup(800,600) #setting window dimensions
t.hideturtle()

home = [0,0]


while True:
    for x in range(360): 
        t.forward(x)
        t.left(40)
        point = t.pos()
        a = m.dist(home,point)
        if a > distance:
            break

turtle.done()








