# Commented out below extraction of colors. Left color_list as final list of colors
# import colorgram

# # Extract colors from image
# colors = colorgram.extract('hirst.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random

turtle.colormode(255)
screen = turtle.Screen()
screen.colormode(255)

trudy = turtle.Turtle()
trudy.speed("fastest")
trudy.penup()
trudy.hideturtle()
color_list = [(240, 248, 245), (234, 242, 248), (236, 225, 82), (202, 5, 72), (198, 165, 9), (235, 50, 131), (207, 75, 11), (111, 179, 216), (218, 162, 103), (235, 224, 5), (12, 23, 62), (30, 188, 108), (23, 106, 173), (16, 28, 176), (218, 132, 177), (9, 186, 215), (229, 167, 198), (209, 26, 144), (123, 189, 161), (8, 49, 28), (36, 133, 73), (125, 219, 233), (65, 21, 7), (112, 89, 212), (191, 15, 5), (143, 216, 200), (235, 62, 36), (74, 9, 28)]

trudy.setheading(225)
trudy.forward(300)
trudy.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    trudy.dot(20, random.choice(color_list))
    trudy.forward(50)

    if dot_count % 10 == 0:
        trudy.setheading(90)
        trudy.forward(50)
        trudy.setheading(180)
        trudy.forward(500)
        trudy.setheading(0)

screen.exitonclick()