import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor('lightgray')

mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)

goal = turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.penup()
goal.speed(0)
# goal.setposition(-100,-100)
goal.setposition(random.randint(-300,300), random.randint(-300,300))


speed = 1

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def isCollision(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor() -t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")



while True:
    player.forward(speed)

    if player.xcor( ) >300 or player.xcor() < -300:
        player.right(180)

    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)

    # d = math.sqrt(math.pow(player.xcor()-goal.xcor(),2) + math.pow(player.ycor() -goal.ycor(),2))
    if isCollision(player,goal):
        goal.setposition(random.randint(-300,300), random.randint(-300,300))
        #goal.hideturtle()


delay = raw_input("Press Enter to finish.")