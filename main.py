import turtle


wn = turtle.Screen()
tess = turtle.Turtle()
angle = 0
for x in range(100):
    tess.forward(50)
    angle += int(x)
    tess.left(angle)
