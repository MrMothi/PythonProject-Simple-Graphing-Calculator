#SimpleGraphingCalculator.py

#The code below imports the needed modules like turtle and random
import random
import turtle
import math


#---Turtle code is a calculator title screen---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import turtle
t = turtle.Turtle()
t.speed(0)
#NEED TO GO FULLSCREEN TO SEE FULL IMAGE 500x500

t.penup()

#Colouring Backround Black 
canvas = turtle.Screen()
canvas.bgcolor ("black") 

#Border
t.penup()
t.forward(500)
t.pendown()
t.pensize(5)
t.pencolor("Cyan")
t.right(90)
t.forward(500)
for i in range(3):
    t.right(90)
    t.forward(1000)
t.right(90)
t.forward(500)
t.penup()

#Going to the centre of the image 
t.goto(0, 0)

#setting the speed and size of the pen
t.speed(0)                                         
t.pensize(6)

#pen and fill colour set for letters
t.pencolor("white")
t.fillcolor("green")

#MOHIT'S----------
#Going to location of "M" in "MOHIT'S"
t.left(180)
t.forward(380)
t.left(90)
t.forward(180)              
t.right(90)
t.forward(60)

#LETTER M-----
#60 Tall 60 wide 
t.pendown()
t.right(180)
t.begin_fill()
for i in range(2):
  t.forward(60)
  t.left(90)
  t.forward(60)
  t.left(90)
t.end_fill()
t.penup()
t.left(90)
t.forward(30)
t.right(90)
t.pendown()
t.forward(20)
t.penup()
t.forward(40)
t.right(90)
t.forward(10)
t.right(90)
t.pendown()
t.forward(20)
t.backward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.penup()

#moving to O
t.right(90)
t.forward(20)
t.left(90)
t.forward(40)
t.right(90)
t.forward(10)

#LETTER O-----
#60 tall 50 wide
t.pendown()
t.begin_fill()
t.right(90)
t.forward(60)
t.left(90)
t.forward(50)
t.left(90)
t.forward(60)
t.left(90)
t.forward(50)
t.end_fill()
t.right(180)
t.forward(25)
t.penup()
t.right(90)
t.forward(20)
t.pendown()
t.forward(20)
t.penup()

#moving to H 
t.left(90)
t.forward(25)
t.left(90)
t.forward(40)
t.right(90)
t.pendown()
t.backward(25)
t.forward(25)
t.penup()
t.forward(10)

#LETTER H-----
# 60 tall 50 wide
t.pendown()
t.begin_fill()
for i in range(2):
  t.forward(50)
  t.right(90)
  t.forward(60)
  t.right(90)
t.end_fill()
t.forward(25)
t.right(90)
t.forward(20)
t.penup()
t.forward(20)
t.pendown()
t.forward(20)
t.right(90)
t.forward(25)
t.right(90)
t.forward(60)
t.penup()

#moving to I
t.right(90)
t.forward(60)

#LETTER I-----
#20 wide 60 high
t.pendown()
t.begin_fill()
for i in range(2):
  t.forward(20)
  t.right(90)
  t.forward(60)
  t.right(90)
t.end_fill()
t.penup()

#moving to T
t.forward(30)

#LETTER T-----
#60 wide 60 tall
t.begin_fill()
t.pendown()
t.forward(60)
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(40)
t.right(90)
t.forward(20)
t.right(90)
t.forward(40)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.end_fill()
t.penup()

#moving to '
t.right(90)
t.forward(70)

#LETTER '-----
#10 wide 20 high
t.pendown()
t.begin_fill()
for i in range(2):
  t.forward(10)
  t.right(90)
  t.forward(20)
  t.right(90)
t.end_fill()
t.penup()

#moving to S
t.forward(20)

#LETTER S
#60 high 50 wide
t.pendown()
t.begin_fill()
for i in range(2):
  t.forward(50)
  t.right(90)
  t.forward(60)
  t.right(90)
t.end_fill()
t.right(90)
t.forward(60)
t.backward(20)
t.left(90)
t.forward(20)
t.penup()
t.forward(30)
t.pendown()
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.backward(20)
t.right(90)
t.forward(20)
t.penup()

#GRAPHER----------
#Moving to G in Grapher
t.goto(0, 0)
t.forward(300)
t.left(90)
t.forward(210)
t.right(90)
t.forward(60)
t.right(90)

#LETTER G-----
#50 wide 60 high
t.pendown()
t.begin_fill()
for i in range(2):
  t.forward(50)
  t.right(90)
  t.forward(60)
  t.right(90)
t.end_fill()
t.forward(50)
t.right(90)
t.forward(30)
t.right(90)
t.forward(25)
t.right(90)
t.forward(15)
t.backward(30)
t.right(90)
t.forward(10)
t.penup()

#moving to letter R
t.forward(15)
t.left(90)
t.forward(45)
t.right(90)
t.forward(10)

#LETTER R-----
#50 wide 60 high
t.pendown()
t.begin_fill()
for i in range(2):
  t.forward(50)
  t.right(90)
  t.forward(60)
  t.right(90)
t.end_fill()
t.forward(25)
t.right(90)
t.penup()
t.forward(10)
t.pendown()
t.forward(12)
t.penup()
t.forward(18)
t.pendown()
t.forward(20)
t.penup()
t.pendown()
t.left(90)
t.forward(25)
t.left(90)
t.forward(30)
t.left(90)
t.forward(15)
t.backward(15)
t.right(90)
t.penup()

#moving to A
t.forward(30)
t.right(90)
t.forward(10)

#LETTER A-----
#50 wide 60 high
t.pendown()
t.begin_fill()
for i in range(2):
  t.forward(50)
  t.right(90)
  t.forward(60)
  t.right(90)
t.end_fill()
t.forward(25)
t.right(90)
t.penup()
t.forward(10)
t.pendown()
t.forward(12)
t.penup()
t.forward(17)
t.pendown()
t.forward(20)
t.penup()

#Moving to P
t.left(90)
t.forward(35)
t.left(90)
t.forward(60)

#LETTER P-----
#50 wide 60 high
t.pendown()
t.begin_fill()
t.right(90)
t.forward(50)
t.right(90)
t.forward(35)
t.right(90)
t.forward(30)
t.left(90)
t.forward(25)
t.right(90)
t.forward(20)
t.right(90)
t.forward(60)
t.end_fill()
t.right(90)
t.forward(25)
t.right(90)
t.penup()
t.forward(10)
t.pendown()
t.forward(10)
t.right(180)
t.penup()

#Moving to H
t.forward(20)
t.right(90)
t.forward(35)

#LETTER H-----
# 60 tall 50 wide
t.pendown()
t.begin_fill()
for i in range(2):
  t.forward(50)
  t.right(90)
  t.forward(60)
  t.right(90)
t.end_fill()
t.forward(25)
t.right(90)
t.forward(20)
t.penup()
t.forward(20)
t.pendown()
t.forward(20)
t.right(90)
t.forward(25)
t.right(90)
t.forward(60)
t.penup()

#Moving to E
t.right(90)
t.forward(60)

#LETTER E-----
t.pendown()
t.pendown()
t.begin_fill()
for i in range(2):
  t.forward(50)
  t.right(90)
  t.forward(60)
  t.right(90)
t.end_fill()
t.forward(50)
t.right(90)
for i in range(2):
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.backward(20)
    t.left(90)
t.penup()

#Moving to R
t.right(180)
t.forward(40)
t.right(90)
t.forward(10)

#LETTER R-----
#50 wide 60 high
t.pendown()
t.begin_fill()
for i in range(2):
  t.forward(50)
  t.right(90)
  t.forward(60)
  t.right(90)
t.end_fill()
t.forward(25)
t.right(90)
t.penup()
t.forward(10)
t.pendown()
t.forward(12)
t.penup()
t.forward(18)
t.pendown()
t.forward(20)
t.penup()
t.pendown()
t.left(90)
t.forward(25)
t.left(90)
t.forward(30)
t.left(90)
t.forward(15)
t.backward(15)
t.right(90)
t.penup()

#Calculator Image----------
#going to centre
t.goto(0, 0)

#Making the Calculator Shape
t.pensize(8)
t.forward(280)
t.right(90)
t.forward(205)
t.pendown()
t.pensize(6)
t.fillcolor("Yellow")
t.begin_fill()
for i in range(2):
    t.right(90)
    t.forward(700)
    t.right(90)
    t.forward(420)
t.end_fill()
t.penup()

#Making calculator screen
t.color("blue")
t.fillcolor("White")
t.backward(10)
t.right(90)
t.forward(10)
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.right(90)
    t.forward(400)
    t.right(90)
t.end_fill()
t.penup()

#Making the buttons--------
t.forward(310)
t.right(90)
t.forward(10)
t.left(90)
t.pencolor("black")
t.pendown()

#top right buttons-----
t.penup()
t.forward(20)
t.pendown()
for a in range(2):
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.right(90)
t.penup()
t.forward(50)
t.pendown()
for a in range(2):
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.right(90)
t.penup()
t.forward(50)
t.pendown()
for a in range(2):
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.right(90)
t.penup()

#bottom box-----
t.forward(70)
t.pendown()
for a in range(2):
    t.forward(170)
    t.right(90)
    t.forward(380)
    t.right(90)

#Bottom right box within bigger box
t.right(90)
for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(170)
    t.left(90)

#Bottom left button in box
t.penup()
t.forward(355)
t.left(90)
for i in range(5):
    t.forward(20)
    t.pendown()
    for i in range(4):
        t.forward(30)
        t.left(90)
    t.penup()
    t.forward(50)
    t.pendown()
    for i in range(4):
        t.forward(30)
        t.left(90)
    t.penup()
    t.forward(50)
    t.pendown()
    for i in range(4):
        t.forward(30)
        t.left(90)
    t.penup()
    t.backward(120)
    t.left(90)
    t.forward(50)
    t.right(90)

#top left buttons
t.penup()
t.right(90)
t.forward(300)
t.right(90)
t.forward(170)
t.right(90)
t.forward(25)
t.pendown()
for i in range(2):
    t.forward(50)
    t.right(90)
    t.forward(130)
    t.right(90)

#top middle buttons
t.penup()
t.goto(0, 0)
t.right(90)
t.forward(90)
t.right(90)
t.pendown()
t.circle(20)
t.penup()
t.right(90)
t.backward(20)
t.left(90)
for i in range(4):
    t.right(90)
    t.penup()
    t.forward(30)
    t.right(90)
    t.forward(15)
    t.pendown()
    for i in range(3):
        t.left(120)
        t.forward(30)
    t.penup()
    t.backward(15)
    t.right(90)
    t.forward(30)

#XY AXIS for parabola
t.speed(15)
t.goto(0, 0)
t.right(90)
t.forward(30)
t.pendown()
t.forward(240)
t.backward(295)
t.goto(0, 0)
t.forward(30)
t.right(90)
t.forward(195)
t.backward(400)
t.goto(0, 30)
t.left(90)
t.penup()

#Parabola
t.speed(3)
t.penup()
t.goto(-1, 3)
h = -1
a = 1
b = 2
c = 4
t.pendown()
t.color("black")
#parabola arm 1 above x = 0
for i in range(50): #the value in the for loop bracket
    x = h + i # to make it more than i
    y = a*(x**2)+(b*x)+(c)
    if y >= -25 and y <= 270 and x >= -200 and x <= 200: 
        t.goto(x, y)
    else:
        break
t.penup()

    #back to minimum or maximum point    #295 high 400 wide
t.goto(-1, 3)
t.pendown()

#parabola arm 1 below x = 0
for i in range(50): #the value in the for loop bracket
    x = h - i # to make it more than i
    y = a*(x**2)+(b*x)+(c)
    if y >= -25 and y <= 270 and x >= -200 and x <= 200:  
        t.goto(x, y)
    else:
        break
t.penup()

#Erase the minigraph
t.speed(0)
t.penup()
t.goto(0, 0)
t.forward(280)
t.right(90)
t.forward(205)
t.color("blue")
t.fillcolor("White")
t.backward(10)
t.right(90)
t.forward(10)
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.right(90)
    t.forward(400)
    t.right(90)
t.end_fill()
t.penup()

#XY AXIS for line
t.speed(15)
t.pencolor("black")
t.goto(0, 0)
t.right(180)
t.forward(30)
t.pendown()
t.forward(240)
t.backward(295)
t.penup()
t.goto(0, 0)
t.pendown()
t.forward(30)
t.right(90)
t.forward(195)
t.backward(400)
t.goto(0, 30)
t.left(90)
t.penup()

#line
t.speed(15)
t.penup()
t.goto(0, b)
t.pendown()
t.color("black")
rise = 1
run = 2
b = 10
#Line side x > 0
for i in range(500): #the value in the for loop bracket
    x = 0 + i # to make it more than i
    y = ((rise/run)*x)+b
    if y >= -25 and y <= 270 and x >= -1950 and x <= 195: 
        t.goto(x, y)
    else:
        break
t.penup()

#back to minimum or maximum point
t.goto(0, b)
t.pendown()

#Line other side x < 0
for i in range(500): #the value in the for loop bracket
    x = 0 - i # to make it more than i
    y = ((rise/run)*x)+b
    if y >= -25 and y <= 270 and x >= -195 and x <= 195:  
        t.goto(x, y)
    else:
        break

#INFO ABOUT Title Page Dimensions-----------------------------------

#Length of MOHIT row: 70 + 60 + 60 + 30 + 70 + 20 + 50
#20 space between MOHIT's row and GRAPHER
#length of GRAPHER row: 60 + 60 + 60 + 60 + 60 + 60 + 60
#Space Between letters is 10
#Top row is 360 wide: MOHIT'S 
#Bottom row is 420 wide: GRAPHER
#Calculator in title page is 700 tall and 420 wide
#The title page calculator screen is 295 high 400 wide

#Going to centre
t.penup()
t.goto(0, 0)

#---------------------Code---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#this variable is for figuring out what calculator the user wants
calculatorType = 0

#Introduction to calculator and type of calculator selector
print("=========================================")
print("-------Welcome to Mohit's Grapher--------")
print("=========================================")

#Simple info about program
print()
print("This calculator could also calculate simple problems aswell!")
print("Enter the numbers you want to use one by one when asked, only numbers please!")
print()
#Asks user what calculator type they want graphing or regular operations
while calculatorType != 1 and calculatorType != 2:
    calculatorType = int(input("We need to know if you need a graphing calculator(1) or a regular calculator for simple operations(2): "))


#---Regular Calculator code looks if the calculatorType is 1-----------------------------------------------------------------------------------------------------------------------------------------------

#--Setting Variables for graphing calculator--

#Defining the function that asks the user if they would like to continue or stop the program
def notdone():
    #Sets variables for the whole time, descriptions of these variables below
    global notDone
    global doneGraphing
    print()
    #below checks when the user wants to stop using this function
    notDone = int(input("Are you done with this function, yes(1), no(0)? "))
    while notDone != 1 and notDone != 0:
        notDone = int(input("Are you done with this function, yes(1), no(0)? "))
    #below asks if the user wants to stop using the program
    if notDone == 1:
        doneGraphing = int(input("Do you want to stop using the calculator? yes(1), no(0)? "))
    while doneGraphing != 1 and doneGraphing != 0:
        doneGraphing = int(input("Do you want to stop using the calculator? yes(1), no(0)? "))
        print()
        
#This variable is for setting what equation the user wants in the equation
equationType = 0
#this is the variable to see if the user is done using the type of quation graphing function
notDone = 0
#this is the variable to determine wether the user wants another graph once they are done thier first
doneGraphing = 0

#checks if the user chose the graphing calculator
if calculatorType == 1:
    print("-------------------------------------------------------------------------------------------------")
    print("You have choosen to use the Graphing calculator!")
    print("The graph area is 500x500, anything outside the area will not appear, though info is still given.")
    print("-------------------------------------------------------------------------------------------------")
#Turtle code to clear title page
    t.screen.bgcolor("White")
    
    #while loop detects when the user is done using the calculator, which would be when the variable will become 1, otherwise it keeps on looking
    while doneGraphing == 0:
        #Sets the notDone variable to 0 as not to end the program when the user switches the type of equation
        notDone = 0
        #turtle code to clear screen
        t.screen.bgcolor("black")
        t.screen.bgcolor("White")
        #clearing the graph
        t.goto(0, 0)
        t.speed(0)
        t.fillcolor("White")
        t.begin_fill()
        t.penup()
        t.forward(500)
        t.pendown()
        t.pensize(5)
        t.pencolor("Cyan")
        t.right(90)
        t.forward(500)
        for i in range(3):
            t.right(90)
            t.forward(1000)
        t.right(90)
        t.forward(500)
        t.penup()
        t.end_fill()
        #back to origin
        t.goto(0, 0)
        t.pendown()
        #Asks for what equation type they want to graph
        equationType = int(input("What type of equation do you want to graph, Standard form(1), vertex form(2), Intercept form(3), Linear(4): "))
        print()


        #-Standard Form-------------------------------------------------
        
        if equationType == 1:
            #tells user that they have chosen the standard form
            print("You have chosen to graph a standard form")
            while notDone == 0:
                #Setting variables needed for standard form
                a = float(input("Enter the a value of the equation: "))
                b = float(input("Enter the b value of the equation: "))
                c = float(input("Enter the c value of the equation: "))
                #finding h
                h = -1*(b) / (2*(a))
                #finding k
                k = a*(h**2)+(b*h)+(c)
                #making the graph
                #draw the axis x and y
                t.goto(0, 0) # go to maximum or minimum point x, y
                t.pensize(3)
                t.speed(0)
                t.pencolor("black")
                t.pendown()
                t.forward(-500)
                t.forward(1000)
                t.forward(-500)                             
                t.left(90)
                t.forward(-500)
                t.forward(1000)
                t.forward(-500)
                t.goto(0, 0)
                
                #Setting Pensize and speed of pen for drawing the user's line
                t.speed(10)
                t.pensize(2)
                
                #making the parabola
                #minimum or maxium point
                t.penup()
                t.goto(h, k)
                t.pendown()
                t.color("black")
                #parabola arm 1 above x = 0
                for i in range(500): #the value in the for loop bracket
                    x = h + i # to make it more than i
                    y = a*(x**2)+(b*x)+(c)
                    if y >= -500 and y <= 500 and x >= -500 and x <= 500: 
                        t.goto(x, y)
                    else:
                        break
                t.penup()

                #back to minimum or maximum point
                t.goto(h, k)
                t.pendown()

                #parabola arm 1 below x = 0
                for i in range(500): #the value in the for loop bracket
                    x = h - i # to make it more than i
                    y = a*(x**2)+(b*x)+(c)
                    if y >= -500 and y <= 500 and x >= -500 and x <= 500:  
                        t.goto(x, y)
                    else:
                        break
                t.penup()
                print("-----Information of Equation-----")

                #Determining wether there will be r and s variables
                if c > 0 and a < 0 or c < 0 and a > 0:
                    #Calculating R and S
                    #Finding the discriminant
                    d = (b**2) - (4*a*c)
                    #Finding r
                    r = (-b -1*(math.sqrt(d)))/(2*a)
                    #finding s
                    s = (-b +1*(math.sqrt(d)))/(2*a)
                    #Telling the user the variables
                    print("The X intercepts of the Eqation are, r: ",round(r, 4),"s: ",round(s, 4))
                else:
                    print("There is no X intercepts for the equation")

                #Determining if the eqation has a minimum or maximum point
                if a > 0:
                    print("The equation has a minimum point, the h is:", h, "the k is:", k)
                else:
                    print("The equation has a maximum point, the h is:", h, "the k is:", k)

                #Printing the y intercept
                print("The y intercept of the equation is:", c)
                #Printing the b variable
                print("The b variable of the equation is:", b)
                #Printing the a variable
                print("The a variable of the equation is:", a)
                print()
                print("Graphing of the Eqaution is Complete")

                #Asking the user if they are done graphing this equation type
                notdone()

                #clearing the graph
                t.goto(0, 0)
                t.fillcolor("White")
                t.begin_fill()
                t.penup()
                t.forward(500)
                t.pendown()
                t.pensize(5)
                t.pencolor("Cyan")
                t.right(90)
                t.forward(500)
                for i in range(3):
                    t.right(90)
                    t.forward(1000)
                t.right(90)
                t.forward(500)
                t.penup()
                t.end_fill()
            #back to origin
            t.goto(0, 0)
            t.pendown()


        #-Vertex Form---------------------------------------------------

        if equationType == 2:
            #tells user that they have chosen the vertex form
            print("You have chosen to graph a vertex form")
            while notDone == 0:
                #Setting variables needed for standard form
                a = float(input("Enter the a value of the equation: "))
                h = float(input("Enter the h value of the equation: "))
                k = float(input("Enter the k value of the equation: "))

                #finding the b and c value
                b = 2*a*h 
                c = a*((h)**2)+k

                #making the graph
                #draw the axis x and y
                t.goto(0, 0) # go to maximum or minimum point x, y
                t.pensize(3)
                t.speed(0)
                t.pencolor("black")
                t.pendown()
                t.forward(-500)
                t.forward(1000)
                t.forward(-500)                             
                t.left(90)
                t.forward(-500)
                t.forward(1000)
                t.forward(-500)
                t.goto(0, 0)
                
                #Setting Pensize and speed of pen for drawing the user's line
                t.speed(10)
                t.pensize(2)
                
                #making the parabola
                #minimum or maxium point
                t.penup()
                t.goto(h, k)
                t.pendown()
                t.color("black")
                #parabola arm 1 above x = 0
                for i in range(500): #the value in the for loop bracket
                    x = h + i # to make it more than i
                    y = a*((x + h)**2)+(k)
                    if y >= -500 and y <= 500 and x >= -500 and x <= 500: 
                        t.goto(x, y)
                    else:
                        break
                t.penup()

                #back to minimum or maximum point
                t.goto(h, k)
                t.pendown()

                #parabola arm 1 below x = 0
                for i in range(500): #the value in the for loop bracket
                    x = h - i # to make it more than i
                    y = a*((x + h)**2)+(k)
                    if y >= -500 and y <= 500 and x >= -500 and x <= 500:  
                        t.goto(x, y)
                    else:
                        break
                t.penup()
                print("-----Information of Equation-----")

                #Determining wether there will be r and s variables
                if c > 0 and a < 0 or c < 0 and a > 0:
                    #Calculating R and S
                    #Finding the discriminant
                    d = (b**2) - (4*a*c)
                    #Finding r
                    r = (-b -1*(math.sqrt(d)))/(2*a)
                    #finding s
                    s = (-b +1*(math.sqrt(d)))/(2*a)
                    #Telling the user the variables
                    print("The X intercepts of the Eqation are, r: ",round(r, 4),"s: ",round(s, 4))
                else:
                    print("There is no X intercepts for the equation")

                #Determining if the eqation has a minimum or maximum point
                if a > 0:
                    print("The equation has a minimum point, the h is:", h, "the k is:", k)
                else:
                    print("The equation has a maximum point, the h is:", h, "the k is:", k)

                #Printing the y intercept
                print("The y intercept of the equation is:", c)
                #printing the b variable
                print("The b variable of the equation is:", b)
                #Printing the a variable
                print("The a variable of the equation is:", a)
                print()
                print("Graphing of the Eqaution is Complete")

                #Asking the user if they are done graphing this equation type
                notdone()

                #clearing the graph
                t.goto(0, 0)
                t.fillcolor("White")
                t.begin_fill()
                t.penup()
                t.forward(500)
                t.pendown()
                t.pensize(5)
                t.pencolor("Cyan")
                t.right(90)
                t.forward(500)
                for i in range(3):
                    t.right(90)
                    t.forward(1000)
                t.right(90)
                t.forward(500)
                t.penup()
                t.end_fill()
            #back to origin
            t.goto(0, 0)
            t.pendown()

            
        #-Intercept Form------------------------------------------------

        if equationType == 3:
            #tells user that they have chosen the intercept form
            print("You have chosen to graph a intercept form")
            while notDone == 0:
                #Setting variables needed for standard form
                a = float(input("Enter the a value of the equation: "))
                r = float(input("Enter the r value of the equation: "))
                s = float(input("Enter the s value of the equation: "))
                #finding h
                h = (r+s)/2
                #finding k
                k = a*((h-s)*(h-r))
                #finding the b and c value
                b = 2*a*h 
                c = a*((h)**2)+k
                
                #making the graph
                #draw the axis x and y
                t.goto(0, 0) # go to maximum or minimum point x, y
                t.pensize(3)
                t.speed(0)
                t.pencolor("black")
                t.pendown()
                t.forward(-500)
                t.forward(1000)
                t.forward(-500)                             
                t.left(90)
                t.forward(-500)
                t.forward(1000)
                t.forward(-500)
                t.goto(0, 0)
                
                #Setting Pensize and speed of pen for drawing the user's line
                t.speed(10)
                t.pensize(2)
                
                #making the parabola
                #minimum or maxium point
                t.penup()
                t.goto(h, k)
                t.pendown()
                t.color("black")
                #parabola arm 1 above x = 0
                for i in range(500): #the value in the for loop bracket
                    x = h + i # to make it more than i
                    y = a*(x-r)*(x-s)
                    if y >= -500 and y <= 500 and x >= -500 and x <= 500: 
                        t.goto(x, y)
                    else:
                        break
                t.penup()

                #back to minimum or maximum point
                t.goto(h, k)
                t.pendown()

                #parabola arm 1 below x = 0
                for i in range(500): #the value in the for loop bracket
                    x = h - i # to make it more than i
                    y = a*(x-r)*(x-s)
                    if y >= -500 and y <= 500 and x >= -500 and x <= 500:  
                        t.goto(x, y)
                    else:
                        break
                t.penup()
                print("-----Information of Equation-----")

                #Determining wether there will be r and s variables
                print("The X intercepts of the Eqation are, r: ",round(r, 4),"s: ",round(s, 4))

                #Determining if the eqation has a minimum or maximum point
                if a > 0:
                    print("The equation has a minimum point, the h is:", h, "the k is:", k)
                else:
                    print("The equation has a maximum point, the h is:", h, "the k is:", k)

                #Printing the y intercept
                print("The y intercept of the equation is:", c)
                #printing the b variable
                print("The b variable of the equation is:", b)
                #Printing the a variable
                print("The a variable of the equation is:", a)
                print()
                print("Graphing of the Eqaution is Complete")

                #Asking the user if they are done graphing this equation type
                notdone()

                #clearing the graph
                t.goto(0, 0)
                t.fillcolor("White")
                t.begin_fill()
                t.penup()
                t.forward(500)
                t.pendown()
                t.pensize(5)
                t.pencolor("Cyan")
                t.right(90)
                t.forward(500)
                for i in range(3):
                    t.right(90)
                    t.forward(1000)
                t.right(90)
                t.forward(500)
                t.penup()
                t.end_fill()
            #back to origin
            t.goto(0, 0)
            t.pendown()

            
        #Linear---------------------------------------------------------
        if equationType == 4:
            #tells user that they have chosen the linear form
            print("You have chosen to graph a intercept form")
            while notDone == 0:
                #Setting variables needed for standard form
                rise = float(input("Enter the rise of the linear equation: "))
                run = float(input("Enter the run of linear the equation: "))
                b = float(input("Enter the b value of the equation: "))
                
                #making the graph
                #draw the axis x and y
                t.goto(0, 0) # go to maximum or minimum point x, y
                t.pensize(3)
                t.speed(0)
                t.pencolor("black")
                t.pendown()
                t.forward(-500)
                t.forward(1000)
                t.forward(-500)                             
                t.left(90)
                t.forward(-500)
                t.forward(1000)
                t.forward(-500)
                t.goto(0, 0)
                
                #Setting Pensize and speed of pen for drawing the user's line
                t.speed(10)
                t.pensize(2)
                
                #making the line
                #Going to the y intercept
                t.penup()
                t.goto(0, b)
                t.pendown()
                t.color("black")
                #Line side x > 0
                for i in range(500): #the value in the for loop bracket
                    x = 0 + i # to make it more than i
                    y = ((rise/run)*x)+b
                    if y >= -500 and y <= 500 and x >= -500 and x <= 500: 
                        t.goto(x, y)
                    else:
                        break
                t.penup()

                #back to minimum or maximum point
                t.goto(0, b)
                t.pendown()

                #Line other side x < 0
                for i in range(500): #the value in the for loop bracket
                    x = 0 - i # to make it more than i
                    y = ((rise/run)*x)+b
                    if y >= -500 and y <= 500 and x >= -500 and x <= 500:  
                        t.goto(x, y)
                    else:
                        break
                t.penup()
                print("-----Information of Equation-----")

                #Finding the M vaule
                m = rise/run
                
                #Printing the y intercept and slope
                print("The y intercept of the equation is:", b)
                #printing the b variable
                print("The slope of the equation is:", m)
                print()
                print("Graphing of the Eqaution is Complete")

                #Asking the user if they are done graphing this equation type
                notdone()

                #clearing the graph
                t.goto(0, 0)
                t.fillcolor("White")
                t.begin_fill()
                t.penup()
                t.forward(500)
                t.pendown()
                t.pensize(5)
                t.pencolor("Cyan")
                t.right(90)
                t.forward(500)
                for i in range(3):
                    t.right(90)
                    t.forward(1000)
                t.right(90)
                t.forward(500)
                t.penup()
                t.end_fill()
            #back to origin
            t.goto(0, 0)
            t.pendown()

    
#Ending statement when the user is done using the Graphing calculator
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Thanks for using Mohit's Grapher!")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


#---Regular Calculator code looks if the calculatorType is 2-----------------------------------------------------------------------------------------------------------------------------------------------

#--Setting Variables for simple calculator--
def notdone():
    global notDone
    global doneOperation
    print()
    #below checks when the user wants to stop using this function
    notDone = int(input("Are you done with this function, yes(1), no(0)? "))
    while notDone != 1 and notDone != 0:
        notDone = int(input("Are you done with this function, yes(1), no(0)? "))
    #below asks if the user wants to stop using the program
    if notDone == 1:
        doneOperation = int(input("Do you want to stop using the calculator? yes(1), no(0)? "))
    while doneOperation != 1 and doneOperation != 0:
        doneOperation = int(input("Do you want to stop using the calculator? yes(1), no(0)? "))
        print()

#below is the variable for selecting what operation for the simple calculator
regOperation = 0
#below is the variable for the calculated number
calculatedNumber = 0
#this is the variable for the first number the user enters
num1 = 0
#this is the variable for the second number the user enters
num2 = 0
#this is the variable to see if the user is done using the simple function
notDone = 0
#this is the variable to determine wether the user wants another operation once they are done thier first
doneOperation = 0

if calculatorType == 2:
    print("----------------------------------------------")
    print("You have choosen to use the simple calculator!")
    print("----------------------------------------------")
    #The while statement below is to let the user come back to the 
    while doneOperation == 0:
        #sets this variable for when the user finishes using an operation
        notDone = 0
        #checks for what operation
        regOperation = int(input("Choose your operation: Multiplication(1), Divsion(2), Subtraction(3), Addition(4): "))
        print()

        #Multiplication-------------------------------------------------
        if regOperation == 1:
            #While statement for seeing if user still needs this function
            while notDone == 0:
                #Asking for the two numbers the user wants
                num1 = float(input("Enter first your number you want to multiply: "))
                num2 = float(input("Enter second your number you want to multiply with: "))
                #Multiplication formula below multiplying the two numbers the user entered
                calculatedNumber = num1 * num2
                #tells user the answer
                print("The product of your entered numbers is,", calculatedNumber)
                notdone()
                
        #Division-------------------------------------------------------
        if regOperation == 2:
            while notDone == 0:
                num1 = float(input("Enter first your number you want to divide: "))
                num2 = float(input("Enter second your number you want to divide with: "))
                calculatedNumber = num1 / num2
                print("The divident of your entered numbers is,", calculatedNumber)
                notdone()


        #Subtraction----------------------------------------------------
        if regOperation == 3:
            while notDone == 0:
                num1 = float(input("Enter first your number you want to subtract: "))
                num2 = float(input("Enter second your number you want to subtract with: "))
                calculatedNumber = num1 - num2
                print("The difference of your entered numbers is,", calculatedNumber)
                notdone()

        #Addition-------------------------------------------------------
        if regOperation == 4:
            while notDone == 0:
                num1 = float(input("Enter first your number you want to add to: "))
                num2 = float(input("Enter second your number you want to add to the first number: "))
                calculatedNumber = num1 + num2
                print("The sum of your entered numbers is,", calculatedNumber)
                notdone()
                    

    #Ending statement when the user is done using the simple calculator
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Thanks for using Mohit's Grapher!")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
