import turtle as t

def turtle_state():
    updown = t.isdown()
    heading = t.heading()
    xcor = t.xcor()
    ycor = t.ycor()
    print("Pen Status :",updown,"\nHeading :",heading, "\nThe coordinates are\nX:",xcor,"\nY:",ycor)


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

    t.goto(80,80)

    square(90, 90, 180)
    square(90, 90, 240)
    square(90, 90, 380)

    turtle_state()
    input("Press enter to continue . . .")

main()



