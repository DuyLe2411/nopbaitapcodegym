angle = int(input("Nhập độ lệch góc bạn chọn: "))
import turtle 
t = turtle.Turtle()
turtle.title("ELIPSE")
t.hideturtle()
turtle.bgcolor("black")
t.pencolor("yellow")
t.speed(0)

ran = int(360/angle)
if 360%angle == 0:
    rad = int(input("Độ cong của hình elipse: "))
    for i in range(ran):
        t.rt(angle)
        for i in range(2):
            t.circle(rad,90)
            t.circle(rad//2,90)
else:
    print("ERROR INPUT")

turtle.done()

