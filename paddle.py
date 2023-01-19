from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_coordinate):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")
        self.goto(x_coordinate, 0)

    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)