from turtle import Turtle
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.goto(0, 180)
        self.write(f"{self.left_score} {self.right_score}", align='center', font=FONT)

    def draw_barrier(self):
        self.goto(0,-300)

        while self.ycor() < 300:
            self.pendown()
            self.sety(self.ycor() + 20)
            self.penup()
            self.sety(self.ycor() + 20)
        self.goto(0, 180)

    def increase_left_score(self):
        self.clear()
        self.draw_barrier()
        self.left_score += 1
        self.write(f"{self.left_score} {self.right_score}", align='center', font=FONT)

    def increase_right_score(self):
        self.clear()
        self.draw_barrier()
        self.right_score += 1
        self.write(f"{self.left_score} {self.right_score}", align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)
