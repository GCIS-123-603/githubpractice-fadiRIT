'''
This is a pixel art drawing program that can quite literally draw any string of values given to it, and is guaranteed to work, even if you have different strings
for each level. And it will keep repeating.

The program mainly has one draw pixel function, and the rest of the color functions which utilize the draw_pixel function with parameters of color, meaning theres
a version of that draw_pixel function that draws black, white, etc.

The main body of the program is in the main() function. 

Firstly it takes input, makes sure it's valid then moves on and begins drawing via checking if conditions for each and draws the appropriate color.
If there is an invalid color entered the program will terminate.

You only have to select from an input of colors that are provided:
0	'black'
1	'white'
2	'red'
3	'yellow'
4	'orange'
5	'green'
6	'yellowgreen'
7	'sienna'
8	'tan'
9	'gray'
A	'darkgray'

using any character outside of those will result in an error.


Something additional is that this program draws differently than the one used in the drawings.py module. We have discovered a more efficient
way to draw pixels and return. We've found many ways to improve from this system and make a different one which can be considered "more optimized".


'''




import turtle


#This function here draws a pixel, and takes color as a parameter/input.
def draw_pixel(color):

    #picking fill color.
    turtle.fillcolor(color)
    
    #picking pencolor.
    turtle.pencolor("black")

    #begin fill.
    turtle.begin_fill()

    #loop that draws the pixel. it starts at the top left of a square, then ends there.
    for i in range(4):
        
        turtle.forward(30)
        turtle.right(90)
    
    #end filling
    turtle.end_fill()

def helperFun1():
    for i in range(2):
            turtle.pencolor("black")
            
            
            draw_pixel("red")
            turtle.forward(30)
            draw_pixel("black")
            turtle.forward(30)

def helperFun2():
     for i in range(5):
            turtle.pencolor("black")
            
            
            draw_pixel("black")
            turtle.forward(30)
            draw_pixel("red")
            turtle.forward(30)
     
#The main function which contains all the executions and activity of the code.
def main():

    #initilization. 
    turtle.penup()
    turtle.goto(-300,300)
    turtle.pendown()

    #The whole program is in a while loop that will continue repeating until False is returned.
    while True:
        #setting speed.
        turtle.speed(5)

        #setting pen color
        turtle.pencolor("black")

        #this will draw.

        for i in range(1):
            turtle.pencolor("black")
            
            helperFun1()
            
                
                
        #penup for resolving semantic errors.
        turtle.penup()
        turtle.penup()
        #turtle.goto(-300,300)
        turtle.pendown()
        #return to initial position.
        turtle.backward(30*4)
        turtle.right(90)
        turtle.forward(30)
        turtle.left(90)
    
#calling main function.
main()