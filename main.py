from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake")

screen.tracer(0)

snake_q = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake_q.up, "Up")
screen.onkey(snake_q.down, "Down")
screen.onkey(snake_q.left, "Left")
screen.onkey(snake_q.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake_q.move()

    # detect the collision between the snake and the food
    if snake_q.head.distance(food) < 15:
        food.refresh()
        snake_q.extend()
        score.update_score()

    # detect collision with wall
    if snake_q.head.xcor() > 285 or snake_q.head.xcor() < -285 or \
            snake_q.head.ycor() > 285 or snake_q.head.ycor() < -285:
        game_is_on = False
        score.game_over()

    # detect tail collision
    for part in snake_q.parts[1:]:  # slicing the list from index 1 to end
        if snake_q.head.distance(part) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
