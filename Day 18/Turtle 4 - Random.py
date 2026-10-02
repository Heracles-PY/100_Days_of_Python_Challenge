from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

trudy = Turtle()
trudy.shape("turtle")
trudy.pensize(10)

def random_color():
    """Generate a random RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for i in range(100):
    steps = random.randint(10, 50)
    angle = random.randint(0, 360)
    trudy.color(random_color())
    trudy.setheading(angle)
    trudy.forward(steps)

screen.exitonclick()