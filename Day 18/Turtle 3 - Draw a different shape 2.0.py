from turtle import Turtle, Screen

trudy = Turtle()
trudy.shape("turtle")
trudy.color("blue")
trudy.pencolor("pink")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        trudy.forward(100)
        trudy.right(angle)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()