from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(3)

        self.x_moving_factor = 1
        self.y_moving_factor = 1

    def move(self):

        self.goto(self.xcor() + (10 * self.x_moving_factor), self.ycor() + (6 * self.y_moving_factor))

    def change_x_moving_factor(self):

        if self.x_moving_factor == 1:
            self.x_moving_factor = -1
        else:
            self.x_moving_factor = 1

    def change_y_moving_factor(self):

        if self.y_moving_factor == 1:
            self.y_moving_factor = -1
        else:
            self.y_moving_factor = 1

    def reset(self):

        self.goto(0, 0)
        self.change_x_moving_factor()