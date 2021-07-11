import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("dark blue")
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

direction = [0, 90, 180, 270]

tim.pensize(15)
tim.speed('fastest')

for i in range(500):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
