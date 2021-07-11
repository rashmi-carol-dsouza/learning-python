from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("dark blue")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(50)
        tim.right(angle)

for shape_side in range (3,20):
    tim.color(random.choice(colours))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()
