# Kelly Sullivan
# Sect 15
# 8 nov 2023
# kls36@email.sc.edu
# Lab 11 Turtle hunting



### import turtle and random 
import turtle
import random

move_counter = 0



#### functions for nemo#####

# functions to turn left and right
def turn_left():
    nemo.left(90)

def turn_right():
    nemo.right(90)


# functions to speed up and down
def speed_up():
    current_speed = nemo.speed()
    global speed
    if speed < 7:
        speed += 1
    

def slow_down():
    current_speed = nemo.speed()
    global speed
    if speed > 1:
        speed -= 1

# function for interesting action (draw a square) when user hits "s"
def draw_square():
    for i in range(4):
        nemo.forward(100)
        nemo.right(90)

        
# send turtle home when space is pressed
def reset_position():
    nemo.penup()
    nemo.goto(0, 0)
    nemo.pendown()
    nemo.speed(3)

#send turtles home when farther than 280
def check_and_reposition():
    x, y = nemo.pos()  
    if abs(x) > 280 or abs(y) > 280:
        nemo.penup()
        nemo.goto(0, 0)  
        nemo.pendown()

def check_and_reposition_predator():
    x, y = predator.pos()
    if abs(x) > 280 or abs(y) > 280:
        predator.penup()
        predator.goto(0, 0)
        
        predator.pen()
        
# move counter
def move_predators():
    global move_counter
    predator.forward(5)
    check_and_reposition_predator()
    if move_counter == 30:
        predator.setheading(random.randint(0, 360))
        move_counter = 0
    else:
            move_counter += 1

#send home turn in circle when caught
def hit_by_predator(nemo, predator):
    if nemo.distance(predator) < 15:
        nemo.penup()
        nemo.goto(0, 0)
        nemo.pendown()
        for _ in range(36):  # Spin 360 degrees
            nemo.right(10)

# set up turtle screen
window = turtle.Screen()
window.bgcolor("white")
window.tracer(3)

# set up turtle
nemo = turtle.Turtle()
nemo.shape("turtle")
speed = nemo.speed()

# predator list
predators = []
for _ in range(3):
    predator = turtle.Turtle()
    predator.shape("arrow")
    predator.color("red")
    predator.penup()
    predator.goto(random.randint(-150, 150), random.randint(-150, 150))
    predator.setheading(random.randint(0,360))
    predator.speed(3)
    predators.append(predator)



#make them move!
running = True
speed = 3
speed2 = 3


# Listen for keyboard events
window.listen()

# Bind arrow keys to turn functions
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")

window.onkey(speed_up, "Up")  
window.onkey(slow_down, "Down")  

window.onkey(reset_position, "space")

window.onkey(draw_square, "s")


# Keep moving and send home


while True:
    nemo.forward(speed)
    for predator in predators:
        predator.forward(speed2)
        move_predators()
        check_and_reposition()
        check_and_reposition_predator()
        hit_by_predator(nemo, predator)

nemo.done()
predator.done()
