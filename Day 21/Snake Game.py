from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

Snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(Snake.up, "Up")
screen.onkey(Snake.down, "Down")
screen.onkey(Snake.left, "Left")
screen.onkey(Snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    Snake.move()

    # Detect collision with food
    if Snake.head.distance(food) < 15:
        food.refresh()
        Snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if Snake.head.xcor() > 300 or Snake.head.xcor() < -300 or Snake.head.ycor() > 300 or Snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in Snake.segments[1:]:
        if Snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()