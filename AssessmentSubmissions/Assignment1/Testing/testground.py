import turtle
import random

def diamond_deco(rec_length,rec_height):
    turtle.pendown()
    colors=['white', 'red','lavender','orange','black'] # making a catalogue of colors 
    turtle.color("black") # so that the colors used are diverse and unique to every runtime o/p

    for k in range(2):
        turtle.begin_fill() 
        turtle.forward(rec_length/4)  
        turtle.right(45)  
        turtle.forward(rec_length/8)  
        turtle.right(135)
        turtle.end_fill() 

        turtle.penup()
        turtle.setheading(270)
        turtle.forward(rec_height/4)
        turtle.setheading(0)


    turtle.penup()


def main():
    diamond_deco(650,50)

    prcoeed = input("Hi")

main()