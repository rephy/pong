from turtle import Turtle

class Scorekeeper(Turtle):

    def __init__(self, paddle):

        super().__init__()

        self.color("white")
        self.hideturtle()
        self.speed(10000)
        self.penup()
        self.goto(200 * (abs(paddle.xcor())/paddle.xcor()), 260)
        self.pendown()

        self.target_paddle = paddle

    def keep_score(self):

        self.clear()
        self.write(self.target_paddle.points, font=("Verdana", 20, "bold"), align="center")