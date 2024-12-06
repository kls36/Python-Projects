# Kelly Sullivan
# Section 15
# 1 Nov 2023
# kls36@email.sc.edu
# Lab 10


import turtle
import random
import time


##define functions

def goleft():
    hunter.setheading(hunter.heading() + 45)

def goright():
    hunter.setheading(hunter.heading() - 45)

    
# set up screen
window = turtle.Screen()
window.bgcolor("lightblue")
window.title("Chasing turtles")
window.setup(width=1000, height=600)
window.tracer(3)

# create turtles

#boundary turtle
boundary = turtle.Turtle()
boundary.hideturtle()
boundary.penup()
boundary.color("red")
boundary.goto(0, -260)
boundary.pendown()
boundary.circle(260)

# hunter turtle
hunter = turtle.Turtle()
hunter.shape("turtle")
hunter.penup()
hunter.color("blue")
hunter.speed(0)
hunter.goto(0,0)

# lives turtle
life = turtle.Turtle()
life.penup()
life.hideturtle()
life.goto(-260, 260)
life.write("Lives: 4", align="left", font=("Arial", 12, "normal"))

# obstacles turtle
obstaclet = turtle.Turtle()
obstaclet.hideturtle()
obstaclet.penup()
obstaclet.speed(6)
obstaclet.color("orange")
obstaclet.hideturtle()

# create obstacle list
obstacles = []

for _ in range(7):
    x = random.uniform(-246, 246)
    y = random.uniform(-260, -20)
    
    while (x**2 + y**2) >= 260**2:
        x = random.uniform(-246, 246)
        y = random.uniform(-260, -20)
    
    obstaclet.goto(x, y)
    obstaclet.begin_fill()
    obstaclet.circle(14)
    obstaclet.end_fill()
    obstacles.append((x, y))


# hunter control
window.listen()

def goleft():
    hunter.setheading(hunter.heading() + 45)

def goright():
    hunter.setheading(hunter.heading() - 45)

window.onkey(goleft, "Left")
window.onkey(goright, "Right")

# set up game variables
lives = 4
time_units = 0

# main game loop

while lives > 0 and time_units < 1250:
    hunter.forward(2)
    
    if hunter.distance(0, 0) > 260:
        lives -= 1
        hunter.goto(0, 0)
        life.clear()
        life.write("Lives: " + str(lives), align="left", font=("Arial", 12, "normal"))
    
    for obstacle in obstacles:
        if hunter.distance(obstacle) < 20:
            lives -= 1
            hunter.goto(0,0)
            life.clear()
            life.write("Lives: " + str(lives), align="left", font=("Arial", 12, "normal"))
    
    time_units += 1

# Game over
if lives == 0:
    life.goto(-260, 240)
    hunter.goto(0, 0)
    life.write("Game Over", align="left", font=("Arial", 20, "normal"))

