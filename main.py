from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time
from food import Food

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.end_game()
    #tail
    for square in snake.squares:
        if square == snake.head:
            pass
        elif snake.head.distance(square) < 10:
            is_game_on = False
            scoreboard.end_game()



screen.exitonclick()
