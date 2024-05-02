from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, paddle_num):

        if paddle_num != 1 and paddle_num != 2:
            raise Exception("Invalid paddle number")

        super().__init__()

        self.color("white")
        self.shape("square")
        self.speed(10000)
        self.penup()
        self.goto(x=(700 * paddle_num - 1050), y=0)
        self.left(90)
        self.shapesize(stretch_len=5)

        self.points = 0
        self.paddle_num = paddle_num

    def reset(self):

        self.goto(x=(700 * self.paddle_num - 1050), y=0)