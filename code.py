# Importing the modules
import turtle
import random

# Code
turtle.bgcolor('black')
turtle.colormode(255)
turtle.speed(0)
for x in range(300):
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    turtle.pencolor(r, g, b)
    turtle.fd(x+50)
    turtle.rt(91)

# Exit
turtle.exitonclick()
