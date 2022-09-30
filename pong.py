# Creating a pong game :

# turtle is a module to help in building graphics of game

import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong by Aniruddh")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0) #to make screen not to update again and agian


# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()  #module.class(name)
paddle_a.speed(0)  #animation speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)  #140px tall, 30px wide
paddle_a.penup()  #to not draw lines
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()  #module.class(name)
paddle_b.speed(0)  #animation speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)  #100px tall, 20px wide
paddle_b.penup()  #to not draw lines
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()  #module.class(name)
ball.speed(0)  #animation speed
ball.shape("circle")
ball.shapesize(stretch_wid = 1, stretch_len = 1)  #20px X 20px
ball.color("white")
ball.penup()  #to not draw lines
ball.goto(0, 0)
ball.dx = 0.2  #d-> change(delta); every time our ball moves with 0.2px
ball.dy = 0.2


# Pen (Write Score)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align = "center", font = ("Courier", 14, "normal"))



# Funciton
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)  #set y to the new y coordinate

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  #listen for the keyboard input (calling the function)
wn.onkeypress(paddle_a_up, "w")  #call function when user press w
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:  #if ball goes above y coordinate = 390(end of upperscreen)
        ball.sety(290)
        ball.dy *= -1  #moves ball to opposite direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:  #if ball goes above y coordinate = 390(end of upperscreen)
        ball.sety(-290)
        ball.dy *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1  #add one point to player A score
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 14, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1  #add one point to player B score
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 14, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1