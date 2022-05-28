from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

# creates the screen and all it's properties
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

# creates the l and r paddle objects from the paddle class
right_paddle = Paddle()
left_paddle = Paddle()

# creates the ping pong ball
ball = Ball()

# moves those paddles to their starting positions
right_paddle.goto(x=350, y=0)
left_paddle.goto(x=-350, y=0)

# adds scoreboard
scoreboard = Scoreboard()
# listens for and binds the key inputs
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_position()











screen.exitonclick()