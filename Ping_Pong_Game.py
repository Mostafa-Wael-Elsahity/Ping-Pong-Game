import turtle



window = turtle.Screen()
window.title("Ping Pong by Mostafa Wael")  # initialize Screen
window.bgcolor("black")  # set color screen
window.setup(width=1280, height=750)  # set coordinate screen
# stop screen updating automatically to control speed Game update
window.tracer(0)

# Racket1
Racket1 = turtle.Turtle()
Racket1.speed(0)  # animation speed
Racket1.shape("square")  # set shape of the object
Racket1.color("red")  # set color of the object
Racket1.penup()  # to remove line due to move of square
Racket1.goto(620, 0)  # set coordinate object
# default size shape 20*20 but we can stretch both wid & len
Racket1.shapesize(stretch_wid=10, stretch_len=1)

# Racket2
Racket2 = turtle.Turtle()
Racket2.speed(0)
Racket2.shape("square")
Racket2.color("blue")
Racket2.penup()  # to remove line due to move of square
Racket2.goto(-620, 0)
Racket2.shapesize(stretch_wid=10, stretch_len=1)
# move Rackets


def Racket1_up():
    Racket1.sety(min(Racket1.ycor()+20, 270))


def Racket1_down():
    Racket1.sety(max(Racket1.ycor()-20, -270))


def Racket2_up():
    Racket2.sety(min(Racket2.ycor()+20, 270))


def Racket2_down():
    Racket2.sety(max(Racket2.ycor()-20, -270))


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()  # to remove line due to move of square
ball.goto(0, 0)
ball.dx = 0.5  # dx delta change x direction
ball.dy = 0.5  # dy delta change y direction

# score
Player1_Score = 0
Player2_Score = 0
score = turtle.Turtle()
score.speed(0)
score.color("green")
score.penup()
score.hideturtle()  # we don't need to see object but we need text show in the object
score.goto(0, 340)
score.write("Player 1: 0 VS Player 2: 0", align="center",
            font=("courier", 24, "normal"))


def close():
    window._delete(all)


# keyboard bindings
window.listen()  # tell the window to expect input
window.onkeypress(Racket1_up, "Up")
window.onkeypress(Racket1_down, "Down")
window.onkeypress(Racket2_up, "w")
window.onkeypress(Racket2_down, "s")
window.onkeypress(close, "E")
winner_player = ""
# main game loop
while True:
    window.update()  # update screen every time in the loop

    # move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # border checker
    if ball.ycor() > 340:  # compare in center of the shape
        ball.sety(340)
        ball.dy *= -1

    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1

    if ball.xcor() > 630:
        ball.goto(0, 0)
        ball.dx *= -1
        Player1_Score += 1

    if ball.xcor() < -630:
        ball.goto(0, 0)
        ball.dx *= -1
        Player2_Score += 1
    score.clear()
    score.write("Blue Player: {} VS Red Player: {}".format(
        Player1_Score, Player2_Score), align="center", font=("courier", 24, "normal"))

    # collision
    if (ball.xcor() > 620 and ball.xcor() < 630) and (abs(ball.ycor()-Racket1.ycor()) <= 100):
        ball.setx(620)
        ball.dx *= -1

    if (ball.xcor() < -620 and ball.xcor() > -630) and (abs(ball.ycor()-Racket2.ycor()) <= 100):
        ball.setx(-620)
        ball.dx *= -1
    if Player1_Score > Player2_Score and Player1_Score > 2:
        winner = "Blue Player win !"
        break

    if Player2_Score > Player1_Score and Player2_Score > 2:
        winner = "Red Player win !"
        break

window.clear()
window.bgcolor("black")
window._write((0, 0), winner, align="center", font=(
    "courier", 36, "normal"), pencolor="gold")
window.delay(1, "m")
