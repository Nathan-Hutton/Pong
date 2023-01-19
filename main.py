from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(800, 600, starty=0)
screen.tracer(0)
screen.listen()

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
scoreboard = Scoreboard()
scoreboard.draw_barrier()
ball = Ball()

screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

while True:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    if ball.horizontal_wall_detection():
        ball.wall_bounce()
    if ball.is_near_paddles() and (right_paddle.distance(ball) <= 50 or left_paddle.distance(ball) <= 50):
        ball.paddle_bounce()
    if ball.left_wall_collision():
        scoreboard.increase_left_score()
        ball.reset()
    elif ball.right_wall_collision():
        scoreboard.increase_right_score()
        ball.reset()
    if scoreboard.left_score == 10 or scoreboard.right_score == 10:
        break


scoreboard.game_over()
screen.exitonclick()
