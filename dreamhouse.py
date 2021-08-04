import turtle
import math
#Đổi thành hình con rùa
#Chỉnh speed, màu cho con rùa
#Màu Background
t = turtle.Turtle()
t.shape("turtle")

turtle.bgcolor("skyblue")
t.speed(0)

#Định dạng vẽ hình chữ nhật
def Rectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.fd(width)
    t.lt(90)
    t.fd(height)
    t.lt(90)
    t.fd(width)
    t.lt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()

#Định dạng vẽ hình tam giác
def triangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.fd(length)
    t.lt(135)
    t.fd(length/math.sqrt(2))
    t.lt(90)
    t.fd(length/math.sqrt(2))
    t.lt(135)
    t.end_fill()

#Định dạng vẽ hình bình hành
def parallelogram(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.lt(30)
    t.fd(width)
    t.lt(60)
    t.fd(height)
    t.lt(120)
    t.fd(width)
    t.lt(60)
    t.fd(height)
    t.lt(90)
    t.end_fill()

#định dạng vẽ ông mặt trời
def drawfourrays(t, length, radius):
    for i in range(4):
        t.penup()
        t.forward(radius)
        t.pendown()
        t.forward(length)
        t.penup()
        t.backward(length + radius)
        t.left(90)







#PHÍA TRƯỚC NHÀ
t.penup()
t.goto(-300,-240)
t.pendown()
t.pensize(3)
Rectangle(t, 200, 220, "blue")
#OK

#Vẽ tam giác mái nhà
t.penup()
t.goto(-300,-20)
t.pendown()
t.pensize(3)
triangle(t, 200, "pink")
#OK
  

#Vẽ cái cửa nhà
t.penup()
t.goto(-230,-240)
t.pendown()
t.pensize(3)
Rectangle(t, 70, 115, "green")
#OK

#Vẽ bên hông ngôi nhà
t.penup()
t.goto(-100,-240)
t.pendown()
t.pensize(3)
parallelogram(t, 120, 220, "yellow")
#OK

#Vẽ cửa sổ
t.penup()
t.goto(-70,-80)
t.pendown()
t.pensize(3)
parallelogram(t, 30, 50, "brown")
#OK

#Vẽ bên hông ngôi nhà
t.penup()
t.goto(-100,-20)
t.pendown()
t.pensize(3)
t.fillcolor("orange")
t.begin_fill()
t.lt(30)
t.fd(120)
t.lt(105)
t.fd(200/math.sqrt(2))
t.lt(75)
t.fd(120)
t.lt(105)
t.fd(200/math.sqrt(2))
t.lt(45)
t.end_fill()
#OK

#VẼ CÁI CÂY
t.penup()
t.goto(300,-250)
t.pendown()
t.pensize(3)
Rectangle(t, 50, 70, "brown" )
#Cái thân cây

#Tán cây
t.penup()
t.goto(225,-180)
t.pendown()
t.pensize(3)
triangle(t, 200, "green")

t.penup()
t.goto(275,-80)
t.pendown()
t.pensize(3)
triangle(t, 100, "green")

t.penup()
t.goto(300,-30)
t.pendown()
t.pensize(3)
triangle(t, 50, "green")

#VẼ ÔNG MẶT TRỜI
t.penup()
t.goto(400,170)
t.pendown()
t.pensize(5)
t.pencolor("red")
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

#VẼ lông cho ông mặt trời
t.penup()
t.goto(400,220)
t.pendown()
t.pensize(5)
t.pencolor("red")
drawfourrays(t ,51, 50)
t.rt(45)
drawfourrays(t, 41, 50)
t.lt(45)


t.penup()
t.goto(-110,-300)
t.pendown()
t.lt(90)
t.fillcolor("white")






turtle.done()



