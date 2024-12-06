# Kelly Sullivan
# Section 15
# 15 Nov 2023
# kls36@email.sc.edu
# Lab 12 Turtle tag


import turtle
import random


#define functions

def turnLeft():
    play.left(30)

def turnRight():
    play.right(30)

def speedUp():
    global player_speed
    if player_speed < 5:
        player_speed += 1

def slowDown():
    global player_speed
    if player_speed > 1:
        player_speed -= 1


# set up screen
screen = turtle.Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("teal")
screen.title("Turtle Tag")
screen.tracer(3)

# writing turtle
invisible = turtle.Turtle()
invisible.speed(0)
invisible.penup()
invisible.hideturtle()
invisible.goto(-300, 300)

# player turtle!
play = turtle.Turtle()
play.speed(2)
play.shape("turtle")
play.shapesize(3)
play.penup()
play.goto(0, 0)

# game turtle 
game = turtle.Turtle()
game.speed(4)
game.shape("circle")
game.shapesize(4)
game.penup()
game.goto(0, 200)

# play controls
screen.listen()
screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.onkey(speedUp, "Up")
screen.onkey(slowDown, "Down")

# game loop!
player_speed = 2
countdown = 500
points = 0

while countdown > 0:
    play.forward(player_speed)
    game.forward(4)

    # bounds!
    if abs(play.xcor()) > 350 or abs(play.ycor()) > 350:
        play.setheading(play.heading() + 180)

    if abs(game.xcor()) > 350 or abs(game.ycor()) > 350:
        game.setheading(game.heading() + 180)

    # collide check
    if play.distance(game) <50:
        points += 1
        play.goto(0, 0)
        game.goto(random.randint(-300, 300), random.randint(-300, 300))

    # countdown and points display
    countdown -= 1
    invisible.clear()
    invisible.write(f"Countdown: {countdown}\nPoints: {points}", align="left", font=("Arial", 12, "normal"))

# Game over
invisible.goto(-300, 0)
invisible.write("Game Over", align="left", font=("Arial", 24, "normal"))



