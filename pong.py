import turtle
import winsound
#from math import *
wn=turtle.Screen() # for showing a screen. small 't' in turtle is for module name and capital 'S' in Screen is for class name.
wn.title("                                                                                                               Pritom Pong ")
turtle.bgcolor("White") # Also can be writen as wn.bgcolor.
turtle.color("white")
wn.setup(width=800,height=600) # in pixel.
wn.tracer(0)  # for stopping update of the window that slow down the screen.
score_a=0
score_b=0
#padle_a
paddle_a=turtle.Turtle() #turtle objects.
paddle_a.speed(0) # set the max speed of the paddle.
paddle_a.shape("square") # Also can be written as turtle.shape.
paddle_a.color("black") # Also can be written as turtle.color.
paddle_a.shapesize(stretch_wid=5,stretch_len=1) # For stretching the shape.
paddle_a.penup() # To avoid the line drawn by the Turtle command.
paddle_a.goto(-380,0) # Where it will have permanent position according to co-ordinate.
#padle_b
paddle_b=turtle.Turtle() #turtle objects.
paddle_b.speed(0) # set the max speed of the paddle.
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup() # To avoid the line drawn by the Turtle command.
paddle_b.goto(373,0)
#ball
ball=turtle.Turtle() #turtle objects.
ball.speed(0) # set the max speed of the paddle.
ball.shape("circle")
ball.color("orange","red")
ball.shapesize(1)
ball.penup() # To avoid the line drawn by the Turtle command.
ball.goto(0,0)
ball.dx=.3
ball.dy=.3
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.goto(0,260)
pen.write("Player A: 0   VS   Player B: 0",align="center",font=("Courier",24,"normal"))
pen.hideturtle()
#Functions
def paddle_a_up():
    y=paddle_a.ycor() # knowing the y co-ordinate of the paddle_a.
    if y<=240:
       y+=20
       paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor() # knowing the y co-ordinate of the paddle_a.
    if y >= -240:
       y-=20
       paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    if y <= 240:
       y+=20
       paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    if y >= -240:
       y-=20
       paddle_b.sety(y)
# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w") # What to do on key press and when.
wn.onkeypress(paddle_a_down,"s") # What to do on key press and when.
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
# Main game loop
while True:
    wn.update()
    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce3.wav", winsound.SND_ASYNC) #winsound.PlaySound("bounce3.wav", winsound.SND_ASYNC
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce3.wav", winsound.SND_ASYNC)
    if ball.xcor()>390:
        #ball.goto(0,0)
        ball.dx*=-1
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
        score_a+=1
        pen.clear()
        pen.write("Player A: {}   VS   Player B: {}".format(score_a,score_b), align="center", font=("Courier", 20, "normal"))
        #"Player A : {} VS Player B : {}".foramt(score_a, score_b)
    if ball.xcor() < -390:
        # ball.goto(0,0)
        ball.dx *= -1
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
        score_b+=1
        pen.clear()
        pen.write("Player A: {}   VS   Player B: {}".format(score_a, score_b), align="center",font=("Courier", 20, "normal"))
    if (ball.xcor() > 353 and ball.xcor() < 363) and  (ball.ycor() <= paddle_b.ycor()+45 and  ball.ycor()>= paddle_b.ycor()-45):
        ball.setx(353)
        ball.dx*=-1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)
    if (ball.xcor()< -360 and ball.xcor()> -370) and  (ball.ycor()<= paddle_a.ycor()+45 and  ball.ycor()>= paddle_a.ycor()-45):
        ball.setx(-360)
        ball.dx*=-1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)

