import turtle
import os
import math
up=0
down=0
#Screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("game")
pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.setposition(-280,-250)
pen.pensize(3)
pen.pencolor("red")
pen.pendown()
for i in range(1,5):
    pen.fd(500)
    pen.lt(90)
pen.hideturtle()

#Walls(Pacman)
w1=turtle.Turtle()
w1.pencolor("blue")
w1.fd(100)
w1.lt(90)
w1.fd(45)
w1.lt(90)
w1.fd(100)
w1.lt(90)
w1.fd(45)
w1.color("blue")
w1.setposition(0,0)
w1.hideturtle()

#player
player=turtle.Turtle()
player.speed(0)
player.penup()
player.shape("circle")
player.color("yellow")
player.setposition(0,-230)
player.setheading(90)
player.speed(1)
playerspeed=15 #Distance moved after key pressed

#Function of player
def move_left():
    x=player.xcor()
    x -=playerspeed
    if x<=-255:
        x=-255
    player.setx(x)
def move_right():
    x=player.xcor()
    x +=playerspeed
    if x>=200:
        x=200
    player.setx(x)
def move_down():
    global up
    up=0
    global down
    down=1
    while(down):
        y=player.ycor()
        y -=playerspeed
        if y<=-250:
            down=0
            up=0
            y=-250
        elif y>=250:
            down=0
            up=0
            y=250
        player.sety(y)
def move_up():
    global down
    down=0
    global up
    up=1
    while(up):
        x=player.xcor()
        y=player.ycor()
        y +=playerspeed
        if y>=-15 and y<255 and x>=0 and x<=115:
            down=0
            up=0
            y=-15
        elif y>=250:
            y=250
            up=0
            down=0
        elif y<=-250:
            y=-250
            up=0
            down=0
        player.sety(y)
        player.setx(x)
#Set key for above functions
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(move_down,"Down")
turtle.onkey(move_up,"Up")













