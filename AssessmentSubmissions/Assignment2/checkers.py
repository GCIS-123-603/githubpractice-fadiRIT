'''
The goal of this program is to make a pixart module that can take input and draw, for example:

Input : 01234
output: Turtle draws pixel by pixel on one colum the following:black,white,gray,brown.

Idea for algorithim:

imagine we have a 5x5:
[][][][][]
[][][][][]
[][][][][]
[][][][][]
[][][][][]


Input for Row 1: "01234"

[0][1][2][3][4]
[][][][][]
[][][][][]
[][][][][]
[][][][][]

Split it into an array or a list : colorsStorage = ["0","1","2","3","4"]
Draw each pixel seperately: for i in range(colorsStorage): drawpixel(30,i)
to accomplish coloration, we can have some sort of relating algorithim
if color == 0:
    draw_black_pixel()
something like that.


'''

import turtle


# This is a test that checks whether the turtle is in the correct place initially. It works!
# we only need to figure out how to make a test take place only at one spot, rather than multiple
def test_InitializeCheckers():
    xcoordinate = int(turtle.xcor())
    ycoordiante = int(turtle.ycor())

    


    assert ycoordiante == 300
    assert xcoordinate == -300
    assert turtle.speed() == 0
    assert turtle.isdown() == False
    assert turtle.pencolor() == "black"
    assert turtle.fillcolor() == "white"
    
def InitializeCheckers():
    #set speed to 0, fastest.
    turtle.speed(0)

    #pen up
    turtle.penup()

    #going into position, top left
    turtle.setheading(0)
    turtle.backward(10*30)
    turtle.left(90)
    turtle.forward(10*30)
    turtle.right(90)

    turtle.pencolor("black")
    turtle.fillcolor("white")
    turtle.pensize(1)

def test_draw_pixel():

    pass

    

def draw_pixel(length,color):
    #setting fill color
    turtle.fillcolor(color)
    
    #put pen down, begin drawing
    turtle.pendown()

    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

def turtle_PixLoop():


    for i in range(20):
        turtle.pendown()
        draw_pixel(30,"brown")
        turtle.forward(30)
    



def main():

    initX = -300
    initY = 300
    InitializeCheckers()

    #test_InitializeCheckers()

    #draw a whole row!
    for i in range(20):
        turtle_PixLoop()
    




    


    wait = input("Enter any key to proceed.")


main()
