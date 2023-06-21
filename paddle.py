from turtle import Turtle

SPEED_Y1 = 40
SPEED_Y2 = 40


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + SPEED_Y1
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - SPEED_Y2
        self.goto(self.xcor(), new_y)

