#Turtle is a basic python program which can be used to draw

# it responds to bSic commands, such as up, to lfit the pen up, and down, to put it down. turtle.up()
# There's also left or right to rotate an amount of degrees, forward to move in the direction its facing a certain distance. turtle.left(90)
# Home to move to the origin, which is 0,0 by default. turtle.home()
# setheading can be used to rotate the turtle to a specific angle. turtle.setheading(180)
# a circle to tell the turtle to draw a circle to its left, not your left.
# turtle_state prints the current state of the turtle.
# turtle.isdown() prints true if pen is down, and false if its up
# turtle.heading( returns the current angle of orientatio nof the turtle
# turtle.xcor(), turtle.ycor() return x and y coordinates of the turtle
# turtle.pencolor() for color
# turtle.pensize(size) for size, turtle.fillcolor(color), turtle.begin_fill, turtle.end_fill()



import turtle as t

def turtle_state():
    updown = t.isdown()
    heading = t.heading()
    xcor = t.xcor()
    ycor = t.ycor()
    print("Pen Status :",updown,"\nHeading :",heading, "\nThe coordinates are\nX:",xcor,"\nY:",ycor)

def testdrive():

    t.pencolor("white")

    t.forward(100)
    t.left(87)
    t.setheading(127)

    t.delay(20)
    t.up()
    
    t.down()
    t.goto(50,50)
    t.home()
    t.circle(25)


parametX = int(input("Pick the X scale for the square!"))
parametY = int(input("Pick the Y scale for the square!"))
parametH = int(input("Select the heading!"))


def square(a, b, c):
    t.up()
    t.goto(100,100)
    t.down()

    t.setheading(c)

    t.pensize(4)
    t.pencolor("red")
    t.fillcolor("blue")


    t.delay(40)
    t.forward(a)
    t.left(b)
    t.forward(a)
    t.left(b)

    t.begin_fill()

    t.forward(a)
    t.left(b)
    t.forward(a)

    t.end_fill()


def main():
    t.bgcolor("black")

    testdrive()
    #square(parametX, parametY, parametH)

    t.goto(80,80)

    square(90, 90, 180)
    square(90, 90, 280)
    square(90, 90, 380)


    turtle_state()
    input("Press enter to continue . . .")

main()
