import turtle
t = turtle.Turtle()
#Khai báo

t.pensize(5)
t.pencolor("blue")
t.speed(0)
#khai báo màu bút, kích cỡ bút
turtle.bgcolor("pink")

#FACE
t.penup()
t.goto(0,-200)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
facesize = 200
t.circle(facesize)
t.end_fill()
#Nhấc bút lên---đi tới điểm M(0,-200)-----đặt bút xuống---vẽ hình tròn bán kính 200

#EYES
t.penup()
t.fillcolor("red")
t.goto(-100,50)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()
#mắt trái

t.penup()
t.goto(100,50)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()
#mắt phải


#NOSE
t.penup()
t.goto(0,50)
t.pendown()
t.pencolor("red")

t.rt(90)
t.fd(60)
t.rt(90)
t.circle(25,180)

#MIỆNG
t.penup()
t.goto(-100,-100)
t.pendown()
t.rt(90)
t.circle(90,180)


turtle.done()
