from turtle import Turtle, Screen

trudy = Turtle()
screen = Screen()

def move_forward():
    trudy.forward(10)

def move_backward():
    trudy.backward(10)

def turn_left():
    new_heading = trudy.heading() + 10
    trudy.setheading(new_heading)

def turn_right():
    new_heading = trudy.heading() - 10
    trudy.setheading(new_heading)

def clear():
    trudy.clear()
    trudy.penup()
    trudy.home()
    trudy.pendown()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()

