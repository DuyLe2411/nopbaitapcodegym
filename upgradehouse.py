import turtle
import math
t = turtle.Turtle()


#Định dạng vẽ hình chữ nhật
def Rectangular(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.fd(width)
    t.rt(90)
    t.fd(height)
    t.rt(90)
    t.fd(width)
    t.rt(90)
    t.fd(height)
    t.rt(90)
    t.end_fill()


#Định dạng vẽ tam giác
def Triangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.fd(length)
    t.lt(135)
    t.fd(length / math.sqrt(2))
    t.lt(90)
    t.fd(length / math.sqrt(2))
    t.lt(135)
    t.end_fill()
#Vẽ cái cây
def tree(t, x, y, length):
    t.penup()
    t.goto(x,y)
    t.pendown()
    Triangle(t, length, "green")
    h1 = y + (math.sqrt((length**2)/2-(length**2)/4))
    t.penup()
    x1 = x + ((3*length)/8)/1.5

    t.goto(x1,h1)
    t.pendown()
    Triangle(t, length/2, "green")
    h2 = h1 + (math.sqrt((length**2)/8-(length**2)/16))
    t.penup()
    x2 = x1 + length/8
    t.goto(x2, h2)
    t.pendown()
    Triangle(t, length/4, "green")


turtle.bgcolor("skyblue")
t.speed(0)
t.pensize(5)
t.pencolor("black")
t.hideturtle()

#Vẽ phía trước ngôi nhà
t.penup()
t.goto(-300,125)
t.pendown()
Rectangular(t, 400, 250, "blue")

#Vẽ cửa ngôi nhà
t.penup()
t.goto(-145,0)
t.pendown()
Rectangular(t, 70, 125, "pink")

#Ve cai mai nha hinh tam giac
t.penup()
t.goto(-300,125)
t.pendown()
Triangle(t, 310, "red")

#Vẽ cái ống khói
t.penup()
t.goto(-72.5, 206)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(35)
t.rt(90)
t.fd(63)
t.lt(90)
t.end_fill()

#Vẽ khói
t.penup()
t.goto(-72.5, 260)
t.pendown()
t.pencolor("brown")
t.lt(90)
t.fd(25)

t.penup()
t.goto(-39, 250)
t.pendown()
t.fd(70)
t.rt(90)

#Vẽ cái cây to(Thân cây---cây)
t.penup()
t.goto(245,-340)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.fd(100)
t.lt(105)
t.fd(89)
t.rt(105)
t.end_fill()
t.penup()
t.goto(245,-340)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.lt(75)
t.fd(89)
t.rt(75)
t.fd(55)
t.end_fill()



#tán cây
tree(t, 200, -250, 200)


#Cái cây nhỏ 2
t.penup()
t.goto(-425, -310)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.fd(50)
t.lt(105)
t.fd(78)
t.rt(105)
t.end_fill()
t.penup()
t.goto(-425, -310)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.lt(75)
t.fd(78)
t.rt(75)
t.fd(25)
t.end_fill()
tree(t, -450, -250, 100)

#Vẽ nắm cửa
t.penup()
t.goto(-95,-64)
t.pendown()
t.fillcolor("magenta")
t.begin_fill()
t.circle(3)
t.end_fill()


turtle.done()