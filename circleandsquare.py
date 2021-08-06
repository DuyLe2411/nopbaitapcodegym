import turtle
t = turtle.Turtle()
shape = input('Circle and square, what is your favorite shape?:')

if shape == 'circle' or shape == 'square':
    color = input('What color will it be?, yellow, red or blue? :')
    
    if color == 'yellow' or color == 'red' or color == 'blue':
        t.fillcolor(color)
        t.begin_fill()
        t.shape(shape)
        t.end_fill()
        turtle.done()
    else:
        print("Sorry, I don't have this color :(")
else:
      print("Sorry, I don't have this shape :(")