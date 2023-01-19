from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.move_speed = 0.01
        self.color("white")
        self.penup()
        self.x_move = 2.5
        self.y_move = 2.5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def horizontal_wall_detection(self):
        if self.ycor() > 280 or self.ycor() < -280:
            return True
        return False

    def left_wall_collision(self):
        if self.xcor() < -390:
            return True
        return False

    def right_wall_collision(self):
        if self.xcor() > 390:
            return True
        return False

    def is_near_paddles(self):
        if self.xcor() >= 328 or self.xcor() <= -328:
            return True

    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.01
