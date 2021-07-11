import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("dark blue")
turtle.colormode(255)
tim.speed('fastest')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
#
# for i in range (70):
#     tim.color(random_color())
#     tim.circle(75)
#     tim.right(5)

# course solution:
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
