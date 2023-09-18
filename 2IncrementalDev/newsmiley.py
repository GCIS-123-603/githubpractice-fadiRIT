import turtle as t

'''
There are multiple steps to drawing a face.
1. Make centered circle, in order to draw a face.
2. Make each eye to be drawn.
3. Nose done by first function.
'''
def options(s,stat):
    t.speed(s)
    t.tracer(stat)


def DrawMainCircle(r,x,y,color):
    
    t.fillcolor(color)

    t.up()
    t.goto(x,y)
    t.forward(r)

    t.down()

    t.begin_fill()
    t.left(90)
    t.circle(r)
    t.end_fill()

    t.left(90)
    t.up()
    t.forward(r)
    t.right(180)

def DrawNose(r,x,y,color):
    DrawMainCircle(r,x,y,color)

def DrawEye(r,x,y,color):

    DrawMainCircle(r/1.2,x,y,color)
    DrawMainCircle(r/2,x,y,"Red")
    DrawMainCircle(r/6,x,y,"Black")

def DrawMouth(r,arc,color):
    t.fillcolor(color)

    t.up()
    t.goto(0,-20)
    t.setheading(90)
    t.left(90)
    t.forward(r)
    t.left(90)
    t.down()

    t.begin_fill()
    t.circle(r,arc)
    t.end_fill()


def DrawMainFace(r,x,y):

    options(12,True)

    DrawMainCircle(r,x,y,"yellow")
    DrawNose(r/10,x,y,"brown")

    DrawEye(r/4,x+30,y+30,"White")
    DrawEye(r/4,x-30,y+30,"White")
    
    t.speed(1)
    DrawMouth(r/2,180,"Blue")
    t.hideturtle()

    proceed = input("Proceed")

DrawMainFace(80,0,0)