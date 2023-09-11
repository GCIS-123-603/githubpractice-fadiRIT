import turtle as t
import random as ran
import re

#THIS IS A RANDOMIZER FOR TESTING.
'''
def randomizer():
    mycolors = ["red", "blue", "yellow", "black"]
    the_color = ran.choices(mycolors)

    mycolors[0] = t.fillcolor("red")
    mycolors[1] = t.fillcolor("blue")
    mycolors[2] = t.fillcolor("yellow")
    mycolors[3] = t.fillcolor("black")

    print(re.sub('\d+', ' ', the_color))

'''




# Incremental Planning Algorithim : Centered Circle.
#
#   ! Assuming (x,y) is the center of the circle, how will we:
#       Move and turn the turtle to position it to draw the circle around the center
# 
#   1. Make sure pen's raised, then setheading to (0,0)
#   2. Move turtle to edge of circle, the radius, (r).
#   3. Turn turtle left 90, and start filling.
#   4. Specify radius, then end fill.
#   5. tests are on



#Draw_Cenetered_Circle, for drawing the circle.
def draw_centered_circle(r, x, y):
    
    t.up()
    t.goto(x,y)
    t.forward(r)

    t.down()

    t.left(90)
    t.circle(r)

    t.left(90)
    t.up()
    t.forward(r)
    t.right(180)

def draw_smiley(r, x, y):
    r = r/2
    draw_centered_circle(r,x,y)




#The Main Function, Testing.
def main():
    t.fillcolor("yellow")
    t.bgcolor("black")
    t.pencolor("red")
    t.delay(25)

    t.begin_fill()
    draw_centered_circle(100,0,0)
    t.end_fill()

    t.fillcolor("orange")
    t.begin_fill()
    draw_smiley(20,0,0)
    t.end_fill()
    t.delay(25)

    proceed=input("Press enter to proceed.")




main()
