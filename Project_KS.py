# kelly Sullivan
#kls36@email.sc.edu
# section 15
# 6 nov 2023
# final- monogram


import turtle

# Function to draw a letter
def draw_letter(turtle, letter):
    if letter == "A":
        turtle.penup()
        turtle.setheading(0)
        turtle.forward(50)
        turtle.pendown()
        turtle.backward(50)
        turtle.setheading(255)
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
        turtle.backward(200)
        turtle.setheading(285)
        turtle.forward(200)
        
        
    elif letter == "B":
        turtle.setheading(90)
        turtle.forward(100)
        turtle.setheading(0)
        turtle.circle(-50, 180)
        turtle.circle(50, -180)
        turtle.setheading(90)
        turtle.forward(100)
        
    elif letter == "C":
        turtle.penup()
        turtle.setheading(0)
        turtle.forward(50)
        turtle.setheading(270)
        turtle.forward(50)
        turtle.pendown()
        turtle.setheading(90)
        turtle.circle(50, -180)
        turtle.backward(100)
        turtle.setheading(270)
        turtle.circle(50, -180)

    elif letter == "D":
        turtle.penup()
        turtle.setheading(270)
        turtle.forward(100)
        turtle.setheading(180)
        turtle.forward(50)
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(200)
        turtle.setheading(180)
        turtle.circle(100, -180)
       
        
    elif letter == "E":
        turtle.penup()
        turtle.setheading(90)
        turtle.forward(100)
        turtle.penup()
        turtle.setheading(180)
        turtle.forward(50)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(75)
        turtle.backward(75)
        turtle.setheading(270)
        turtle.forward(100)
        turtle.setheading(0)
        turtle.forward(75)
        turtle.backward(75)
        turtle.setheading(270)
        turtle.forward(100)
        turtle.setheading(0)
        turtle.forward(75)
        turtle.backward(75)
        
    elif letter == "F":
        turtle.penup()
        turtle.setheading(90)
        turtle.forward(100)
        turtle.penup()
        turtle.setheading(180)
        turtle.forward(50)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(75)
        turtle.backward(75)
        turtle.setheading(270)
        turtle.forward(100)
        turtle.setheading(0)
        turtle.forward(75)
        turtle.backward(75)
        turtle.setheading(270)
        turtle.forward(100)
        
    elif letter == "G":
        turtle.penup()
        turtle.setheading(0)
        turtle.forward(50)
        turtle.setheading(270)
        turtle.forward(50)
        turtle.pendown()
        turtle.setheading(0)
        turtle.backward(40)
        turtle.forward(40)
        turtle.setheading(90)
        turtle.circle(50, -180)
        turtle.backward(100)
        turtle.setheading(270)
        turtle.circle(50, -180)
        
        
    elif letter == "H":
        turtle.setheading(0)
        turtle.forward(35)
        turtle.backward(70)
        turtle.setheading(90)
        turtle.forward(100)
        turtle.backward(200)
        turtle.penup()
        turtle.setheading(0)
        turtle.forward(70)
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(200)

        
    elif letter == "I":
        turtle.setheading(270)
        turtle.forward(100)
        turtle.setheading(0)
        turtle.backward(25)
        turtle.forward(50)
        turtle.backward(25)
        turtle.setheading(90)
        turtle.forward(200)
        turtle.setheading(0)
        turtle.backward(25)
        turtle.forward(50)
        turtle.backward(25)
        
    elif letter == "J":
        turtle.penup()
        turtle.setheading(0)
        turtle.forward(50)
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(100)
        turtle.backward(150)
        turtle.circle(50, -180)
        
    elif letter == "K":
        turtle.setheading(90)
        turtle.forward(100)
        turtle.backward(200)
        turtle.forward(100)
        turtle.setheading(60)
        turtle.forward(113)
        turtle.backward(113)
        turtle.setheading(300)
        turtle.forward(113)
        turtle.backward(113)
        
        
    elif letter == "L":
        turtle.setheading(0)
        turtle.penup()
        turtle.forward(35)
        turtle.setheading(270)
        turtle.forward(100)
        turtle.pendown()
        turtle.setheading(0)
        turtle.backward(70)
        turtle.setheading(90)
        turtle.forward(200)
        
        
    elif letter == "M":
        turtle.penup()
        turtle.setheading(180)
        turtle.forward(50)
        turtle.setheading(270)
        turtle.forward(100)
        turtle.pendown()
        turtle.backward(200)
        turtle.setheading(300)
        turtle.forward(100)
        turtle.setheading(60)
        turtle.forward(100)
        turtle.setheading(270)
        turtle.forward(200)
        
    elif letter == "N":
        turtle.penup()
        turtle.setheading(180)
        turtle.forward(50)
        turtle.setheading(270)
        turtle.forward(100)
        turtle.pendown()
        turtle.backward(200)
        turtle.setheading(296)
        turtle.forward(225)
        turtle.setheading(90)
        turtle.forward(200)
        
    elif letter == "O":
        turtle.penup()
        turtle.setheading(0)
        turtle.forward(50)
        turtle.setheading(270)
        turtle.forward(50)
        turtle.pendown()
        turtle.setheading(90)
        turtle.circle(50, -180)
        turtle.backward(100)
        turtle.setheading(270)
        turtle.circle(50, -180)
        turtle.setheading(270)
        turtle.forward(100)
        
        
    elif letter == 'P':
        turtle.setheading(90)
        turtle.forward(100)
        turtle.setheading(0)
        turtle.circle(-50, 180)
        turtle.penup()
        turtle.circle(50, -180)
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(100)
        
    elif letter == 'Q':
        turtle.penup()
        turtle.setheading(0)
        turtle.forward(50)
        turtle.setheading(270)
        turtle.forward(50)
        turtle.pendown()
        turtle.setheading(90)
        turtle.circle(50, -180)
        turtle.backward(100)
        turtle.setheading(270)
        turtle.circle(50, -180)
        turtle.setheading(270)
        turtle.forward(100)
        turtle.penup()
        turtle.forward(25)
        turtle.setheading(315)
        turtle.pendown()
        turtle.forward(15)
        turtle.backward(45)

        
    elif letter == 'R':
        turtle.setheading(90)
        turtle.forward(100)
        turtle.setheading(0)
        turtle.circle(-50, 180)
        turtle.setheading(300)
        turtle.forward(113)
        turtle.backward(113)
        turtle.setheading(270)
        turtle.forward(100)
        
    elif letter == 'S':
        turtle.setheading(0)
        turtle.circle(50, -180)
        turtle.backward(20)
        turtle.forward(20)
        turtle.circle(50, 180)
        turtle.setheading(180)
        turtle.circle(50, -180)
        turtle.backward(20)
        turtle.forward(20)
        
        
    elif letter == 'T':
        turtle.setheading(270)
        turtle.forward(100)
        turtle.setheading(90)
        turtle.forward(200)
        turtle.setheading(0)
        turtle.backward(35)
        turtle.forward(70)
        turtle.backward(35)
        
    elif letter == 'U':
        turtle.penup()
        turtle.setheading(0)
        turtle.forward(50)
        turtle.setheading(270)
        turtle.forward(55)
        turtle.pendown()
        turtle.backward(150)
        turtle.forward(150)
        turtle.setheading(90)
        turtle.circle(50, -180)
        turtle.backward(150)
        
    elif letter == 'V':
        turtle.setheading(270)
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
        turtle.setheading(105)
        turtle.forward(206)
        turtle.backward(206)
        turtle.setheading(75)
        turtle.forward(206)
        turtle.backward(206)
        
    elif letter == 'W':
        turtle.penup()
        turtle.setheading(180)
        turtle.forward(50)
        turtle.setheading(90)
        turtle.forward(100)
        turtle.pendown()
        turtle.backward(200)
        turtle.setheading(60)
        turtle.forward(100)
        turtle.setheading(300)
        turtle.forward(100)
        turtle.setheading(270)
        turtle.backward(200)
        
        
    elif letter == 'X':
        turtle.setheading(296)
        turtle.backward(112)
        turtle.forward(224)
        turtle.backward(112)
        turtle.setheading(244)
        turtle.backward(112)
        turtle.forward(224)
        turtle.backward(112)
        
    elif letter == 'Y':
        turtle.setheading(296)
        turtle.backward(112)
        turtle.forward(112)
        turtle.setheading(244)
        turtle.backward(112)
        turtle.forward(112)
        turtle.setheading(270)
        turtle.forward(100)
        
        
    elif letter == 'Z':
        turtle.setheading(244)
        turtle.backward(112)
        turtle.forward(224)
        turtle.setheading(0)
        turtle.forward(100)
        turtle.backward(100)
        turtle.setheading(244)
        turtle.backward(224)
        turtle.setheading(0)
        turtle.backward(100)



########Done with alphabet########
        
        








# Get user input for favorite color and initials- set up variables
fav_color1 = input("Enter your favorite color: ")
fav_color = fav_color1.lower()
if fav_color == "purple":
    fav_color == "violet"

initial = input("Enter your initials: ")
initials = initial.upper()



# Set up the Turtle window
screen = turtle.Screen()
screen.bgcolor(f"{fav_color}4")
screen.tracer(0)



# Create three Turtle objects
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()

#border turtle
border = turtle.Turtle()
border.color("white")
border.penup()
border.pensize(9)
border.goto(-250,-150)
border.pendown()
border.begin_fill()
border.setheading(0)
border.forward(500)
border.setheading(90)
border.forward(300)
border.setheading(180)
border.forward(500)
border.setheading(270)
border.forward(300)
border.end_fill()
border.color("black")
border.pensize(13)
border.setheading(0)
border.forward(500)
border.setheading(90)
border.forward(300)
border.setheading(180)
border.forward(500)
border.setheading(270)
border.forward(300)
border.color("white")
border.pensize(2)
border.setheading(0)
border.forward(500)
border.setheading(90)
border.forward(300)
border.setheading(180)
border.forward(500)
border.setheading(270)
border.forward(300)
border.hideturtle()
screen.tracer(1)



# Set up turtles' positions
turtle1.pensize(9)
turtle1.penup()
turtle1.goto(-115, -5)
turtle1.pendown()

turtle2.pensize(9)
turtle2.penup()
turtle2.goto(-5, -5)
turtle2.pendown()

turtle3.pensize(9)
turtle3.penup()
turtle3.goto(105, -5)
turtle3.pendown()

# Set up turtles' colors
turtle1.color("black")
turtle2.color("black")
turtle3.color("black")


# Draw each letter of the initials using a different turtle
draw_letter(turtle1, initials[0])
draw_letter(turtle2, initials[1])
draw_letter(turtle3, initials[2])

# Set up turtles' positions
turtle1.penup()
turtle1.goto(-110, 0)
turtle1.pendown()

turtle2.penup()
turtle2.goto(0, 0)
turtle2.pendown()

turtle3.penup()
turtle3.goto(110, 0)
turtle3.pendown()

# Set up turtles' colors
turtle1.color(f"{fav_color}2")
turtle2.color(f"{fav_color}2")
turtle3.color(f"{fav_color}2")


# Draw each letter of the initials using a different turtle
draw_letter(turtle1, initials[0])
draw_letter(turtle2, initials[1])
draw_letter(turtle3, initials[2])

####make them draw again
turtle1.penup()
turtle1.goto(-105, 5)
turtle1.pendown()

turtle2.pensize(9)
turtle2.penup()
turtle2.goto(5, 5)
turtle2.pendown()

turtle3.pensize(9)
turtle3.penup()
turtle3.goto(115, 5)
turtle3.pendown()

# Set up turtles' colors
turtle1.color(fav_color)
turtle2.color(fav_color)
turtle3.color(fav_color)

# Draw each letter of the initials using a different turtle
draw_letter(turtle1, initials[0])
draw_letter(turtle2, initials[1])
draw_letter(turtle3, initials[2])



turtle1.hideturtle()
turtle2.hideturtle()
turtle3.hideturtle()
