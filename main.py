from time import sleep

from turtle import Screen
from paddle import Paddle
from scorekeeper import Scorekeeper
from ball import Ball

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong - by Raphael Manayon")
screen.tracer(0)

paddle1 = Paddle(1)
paddle2 = Paddle(2)

paddle1_scorekeeper = Scorekeeper(paddle1)
paddle2_scorekeeper = Scorekeeper(paddle2)

ball = Ball()

game = True

delay = 0.05

def paddle1_up():

    if paddle1.ycor() < 230:
        paddle1.forward(20)

def paddle1_down():

    if paddle1.ycor() > -230:
        paddle1.backward(20)

def paddle2_up():

    if paddle2.ycor() < 230:
        paddle2.forward(20)

def paddle2_down():

    if paddle2.ycor() > -230:
        paddle2.backward(20)

screen.listen()

screen.onkey(key="w", fun=paddle1_up)
screen.onkey(key="s", fun=paddle1_down)
screen.onkey(key="Up", fun=paddle2_up)
screen.onkey(key="Down", fun=paddle2_down)

paddle1_scorekeeper.keep_score()
paddle2_scorekeeper.keep_score()

while game:
    sleep(delay)
    screen.update()
    ball.move()

    if abs(ball.ycor()) >= 290:
        ball.change_y_moving_factor()

    if 390 >= abs(ball.xcor()) >= 330:
        print(abs(abs(ball.ycor()) - abs(paddle2.ycor())), abs(abs(ball.ycor()) - abs(paddle1.ycor())))

        if abs(abs(ball.ycor()) - abs(paddle2.ycor())) <= 50 and ball.x_moving_factor != -1:
            ball.change_x_moving_factor()
            delay *= 0.95

        if abs(abs(ball.ycor()) - abs(paddle1.ycor())) <= 50 and ball.x_moving_factor != 1:
            ball.change_x_moving_factor()
            delay *= 0.95

    if ball.xcor() > 410:
        paddle1.points += 1
        paddle1_scorekeeper.keep_score()
        paddle2_scorekeeper.keep_score()
        screen.update()
        delay = 0.05
        sleep(3)

        paddle1.reset()
        paddle2.reset()
        ball.reset()
    elif ball.xcor() < -410:
        paddle2.points += 1
        paddle1_scorekeeper.keep_score()
        paddle2_scorekeeper.keep_score()
        screen.update()
        delay = 0.05
        sleep(3)

        paddle1.reset()
        paddle2.reset()
        ball.reset()

screen.exitonclick()