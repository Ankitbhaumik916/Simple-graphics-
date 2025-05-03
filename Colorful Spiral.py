import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

hue = 0
t.pensize(2)

for i in range(360):
    col = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(col)
    t.forward(i * 3 / 5 + i)
    t.left(59)
    t.circle(5)
    hue += 0.005

turtle.done()
