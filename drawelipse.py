angle = int(input("Nhập độ lệch góc bạn chọn: "))
import turtle 
import random as r
t = turtle.Turtle()
turtle.title("ELIPSE")
t.hideturtle()
turtle.bgcolor("black")

t.speed(0)
color_list = ["green","purple","light blue","sky blue","light green","red","pink","yellow","brown","silver"]
ran = int(360/angle)
if 360%angle == 0:
    rad = int(input("Độ cong của hình elipse: "))
    for i in range(ran):
        t.rt(angle)
        color = r.choice(list(color_list))
        t.pencolor(color)
        for i in range(2):
            t.circle(rad,90)
            t.circle(rad//2,90)
else:
    print("ERROR INPUT")

turtle.done()

