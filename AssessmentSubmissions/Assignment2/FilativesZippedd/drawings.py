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

There are a few tests utilized.


'''




import turtle


#The following tests mainly check the configuration of a file

#test that pencolor is black at all times
def test_main_config():
    assert turtle.pencolor() == "black"

#test position correction

def test_second_config():
    assert round(turtle.xcor()) == -300 #its supposed to be -300, but theres an issue with the number. 

#test pen size unchanging
def test_third_config():
    assert turtle.pensize() == 1

#testing coloration of a pixel
def test_draw_pixel_color():
    turtle.clear()
    red_Pixel()
    assert turtle.fillcolor() == "red"

def test_heading():
    turtle.clear()
    draw_pixel("blue")
    assert turtle.heading() == 0

def test_InitializeCheckers():

    assert turtle.isdown() == True


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


#All of the functions below are for coloring the pixels, very simple and straightforward.
#Each of them are designated a string or a value, which is in a comment above them.
#0
def black_Pixel():
    draw_pixel("black")
#1
def white_Pixel():
    draw_pixel("white")
#2
def red_Pixel():
    draw_pixel("red")
#3
def yellow_Pixel():
    draw_pixel("yellow")
#4
def orange_Pixel():
    draw_pixel("orange")
#5
def green_Pixel():
    draw_pixel("green")
#6
def greenYel_Pixel():
    draw_pixel("yellowgreen")
#7
def sienna_Pixel():
    draw_pixel("sienna")
#8
def tan_Pixel():
    draw_pixel("tan")
#9
def gray_Pixel():
    draw_pixel("gray")
#A
def darkgray_pixel():
    draw_pixel("darkgray")


#The main function which contains all the executions and activity of the code.
def main():

    #initilization. 
    turtle.penup()
    turtle.goto(-300,300)
    turtle.pendown()

    #The whole program is in a while loop that will continue repeating until False is returned.
    while True != "q":
        #setting speed.
        turtle.speed(0)

        #taking input for the file contents.
        inputStuff = input("Input your string to be drawn. Press 'q' to quit.\n")

        #setting pen color
        turtle.pencolor("black")

        #making sure pen does not have spaces or empty whitespace of any form.
        if inputStuff.strip() == "":
            print("Entry Error. \n \t \t \t ---> Please enter a non-whitespace value!")

            #skips over full loop and gives input again.
            continue

        #takes length of string so it can go back to original position after drawing
        lengthOfstring = len(inputStuff)

        #this will take a string, first loop goes into sentences, then second loop goes into the words then it prints
        for x in inputStuff:
            turtle.pencolor("black")
            for word in x.split():
                turtle.pencolor("black")

                #a list of if statements that decide which color/pixel is going to be drawn.
                if word == "0":
                    black_Pixel()
                    turtle.pencolor("black")
                    turtle.forward(30)
                elif word == "1":
                    white_Pixel()
                    turtle.pencolor("black")
                    turtle.forward(30)
                elif word == "2":
                    red_Pixel()
                    turtle.pencolor("black")
                    turtle.forward(30)
                elif word == "3":
                    yellow_Pixel()
                    turtle.pencolor("black")
                    turtle.forward(30)
                elif word == "4":
                    orange_Pixel()
                    turtle.pencolor("black")
                    turtle.forward(30)
                elif word == "5":
                    green_Pixel()
                    turtle.pencolor("black")
                    turtle.forward(30)
                elif word == "6":
                    greenYel_Pixel()
                    turtle.pencolor("black")
                    turtle.forward(30)
                elif word == "7":
                    sienna_Pixel()
                    turtle.pencolor("black")
                    turtle.forward(30)
                elif word == "8":
                    tan_Pixel()
                    turtle.pencolor("black")
                    turtle.forward(30)
                elif word == "9":
                    gray_Pixel()
                    turtle.pencolor("black")
                    turtle.forward(30)
                elif word == "A":
                    darkgray_pixel()
                    turtle.pencolor("black")
                    turtle.forward(30)
                elif word == "q":
                    print("Exiting Program.")
                    return False
                else:
                    #this is incase of an error where an invalid color/character is entered. the program will terminate.
                    print("Error! Invalid Color. \n \t \t \t ---> PROGRAM TERMINATING.")
                    return False
                
                
        
        #penup for resolving semantic errors.
        turtle.penup()
        turtle.penup()
        #turtle.goto(-300,300)
        turtle.pendown()
        #return to initial position by using previous length of string, so doesnt have to be limited to 20x20.
        turtle.backward(30*lengthOfstring)
        turtle.right(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.pendown()
    
#calling main function.
main()