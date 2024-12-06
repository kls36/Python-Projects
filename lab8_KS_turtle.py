# Kelly Sullivan
# Sect. 15
# 18 Oct 2023
# kls36@email.sc.edu
# Lab 8- Turtle circles

import turtle
import random

#set up screen
window = turtle.Screen()
window.bgcolor("green")

# my variables

speed = 6
counter = 0
maxTurtles = 6


#list of turtles
turtles = []
for i in range(maxTurtles):
    #set up turtle
    t = turtle.Turtle()
    t.shape("turtle")
    t.width(2)
    t.color("black")
    # add to list 
    turtles.append(t)
    #random position
    turtles[i].penup()
    turtles[i].goto(random.randint(-100,100), random.randint(-100,100))
    turtles[i].setheading(random.randint(0,360))
    turtles[i].speed(6)
    turtles[i].pendown()

#set up the loop
while counter < 300:
    for i in range(maxTurtles):
        turtles[i].forward(speed) #make the turtle move
        if turtles[i].distance(0,0) > 200:
            turtles[i].left(90) # keep on screen
        if counter % 30 == 0:
            turtles[i].right(random.randint(0, 360))#random directiom
        if counter % 20 == 0:
            colors = ["red", "blue", "pink"] #change color and run around
            turtles[i].color(random.choice(colors))
            turtles[i].begin_fill()
            turtles[i].circle(50)
            turtles[i].end_fill()
            turtles[i].color("black")
       
    
    counter += 1

turtle.done()        
