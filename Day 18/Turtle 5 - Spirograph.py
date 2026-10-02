import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)

# Turtle setup
artist = turtle.Turtle()
artist.speed("fastest")
artist.pensize(3)

def random_color():
    """Generate a random RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(gap_size, radius):
    """Draw a spirograph with a given angular step and circle size."""
    for _ in range(int(360 / gap_size)):
        artist.color(random_color())
        artist.circle(radius)
        artist.setheading(artist.heading() + gap_size)

# Draw the pattern (5-degree shift per circle, 100-pixel radius)
draw_spirograph(gap_size=5, radius=100)

artist.hideturtle()
screen.exitonclick()