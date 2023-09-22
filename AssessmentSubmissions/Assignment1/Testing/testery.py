import turtle


def drawTriangle(length,height):

    #pen is up
    turtle.penup()

   

    #pen now down
    turtle.pendown()

    #begin drawing.
    turtle.forward(length)  
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.setheading(0)

    #pen up, first triangle drawn.
    turtle.penup()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length/2)
    #going into position


    #pen down, drawing begin
    turtle.pendown()

    #begin drawing
    turtle.setheading(240)
    turtle.forward(length)
    turtle.setheading(120)
    turtle.forward(length)
    turtle.setheading(0)
    turtle.forward(length)

    #drawing done, penup.
    turtle.penup()

    #going back to origin.
    turtle.backward(length/2)
    turtle.setheading(270)
    turtle.forward(length/2)
    turtle.setheading(0)


 


drawTriangle(100,10)