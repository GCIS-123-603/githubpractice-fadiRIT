import turtle


# This is a test that checks whether the turtle is in the correct place initially. It works!
# we only need to figure out how to make a test take place only at one spot, rather than multiple

turtle.speed(0)
listed_color = []
def openFile():
    with open("./Filatives/drawing04.txt") as turtleDrawing:

        readlines = turtleDrawing.readlines()

        for i in readlines:
            
            for char in i:
                listed_color.append(char)



def draw_pixel(length,color):
    #setting fill color
    turtle.fillcolor(color)
    
    #put pen down, begin drawing
    turtle.pendown()

    turtle.begin_fill()
    
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)
    
    turtle.end_fill()

#COLORED PIXELS FUNCTIONS

def blackPixel():
    #0
    draw_pixel(30,"black")

def whitePixel():
    #1
    draw_pixel(30,"white")




def main():

    #go into org position
    turtle.penup()
    turtle.goto(-300,300)
    turtle.pendown()




        #draw full checker!
    for i in range(20):
        for i in range(20):
            
            for x in listed_color:
                if x == "0":
                    blackPixel()
                    turtle.forward(30)
            
        if turtle.heading() == 270:
            turtle.left(90)
            turtle.forward(60)
            turtle.left(90)
        elif turtle.heading() == 0:
            pass
            #turtle.right(90)
            #turtle.forward(60)
            #turtle.right(90)
        elif turtle.heading() == 180:
            turtle.left(90)
            turtle.left(90)




    


    wait = input("Enter any key to proceed.")


main()
