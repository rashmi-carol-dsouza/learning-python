import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('images.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(115, 91, 67), (175, 156, 133), (70, 88, 122), (26, 39, 59), (57, 42, 25), (108, 80, 93), (53, 33, 46), (25, 49, 37), (171, 153, 161), (230, 220, 228), (74, 96, 83), (136, 154, 181), (45, 54, 102), (227, 217, 204), (157, 138, 78), (82, 71, 32), (95, 109, 186), (217, 199, 136), (38, 78, 64), (86, 50, 66), (147, 160, 151), (95, 51, 41), (161, 106, 124), (173, 107, 95), (218, 229, 222), (32, 76, 86), (185, 184, 211), (210, 179, 194), (217, 180, 172)]
import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.hideturtle()
turtle.colormode(255)
tim.speed('fastest')
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()
