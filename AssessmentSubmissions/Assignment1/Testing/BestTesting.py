import turtle
import random


'''
11:15pm, 9/18/23

I stopped here after making excellent code which works, and takes a color for each layer.
the only thing you need to work on is :

fixing candle drawing

fixing normal decoration and finding a way to make it equally spread based on length, perhaps make a function that will check if it can be split into 4, and if it can
it'll be done in a certain way every certain pixels, etc.

make sure everything works, set maxs and minimums for the input values as well.


setting up inputs,FINAL

'''

#DIAMOND DECO NEEDS REMAKE  
def diamond_deco(rec_length,rec_height):
    turtle.pendown()
    colors=['white', 'red','lavender','orange','black'] # making a catalogue of colors 
    turtle.color(random.choice(colors)) # so that the colors used are diverse and unique to every runtime o/p

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

def candle(): #comes after cake_base func
    #pen is still up
    turtle.color('purple')
    
    #moving into position
    turtle.left(90)
    turtle.forward(30)
    x=turtle.xcor() #getting the coordinates to reuse later to posiition stylus to draw the decorations
    y=turtle.ycor() #getting the coordinates to reuse later to posiition stylus to draw the decorations
    turtle.pendown() 

    #taking the length as 10 and breadth as 100
    turtle.begin_fill()
    for i in range(2): #drawing and filling the candle
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()

    #flame 
    #pen is down

def candlette(length,height,radius):

    #fill color pick
    turtle.fillcolor("gray")

    #going back to original heading
    turtle.setheading(0)

    #pen is up
    turtle.penup()

    #going into position
    turtle.forward(height/14)
    turtle.left(90)
    
    #now in position

    #pen down, drawing begin.
    turtle.pendown()

    #fill begin
    turtle.begin_fill()

    turtle.forward(height/2)
    turtle.left(90)
    turtle.forward(length/40)
    turtle.left(90)
    turtle.forward(height/2)

    #fill end
    turtle.end_fill()

    #pen is up
    turtle.penup()

    #going back into position to draw flame
    turtle.left(90)
    turtle.forward(length/80)
    turtle.left(90)
    turtle.forward(height/2)
    #now in position

    #begin drawing
    turtle.forward(radius)
    turtle.right(90)
    turtle.forward(radius)
    

    #color select for flame
    turtle.fillcolor("yellow")

    #begin fil flame
    turtle.begin_fill()

    #pen down, drawing begin
    turtle.pendown()
    turtle.left(90)

    #draw circle for flame
    turtle.circle(radius)

    #end fill, drawing end.
    turtle.end_fill()
   
    #pen up, drawing complete.
    turtle.penup()

    


    #drawing complete


def draw_rectangle(length,height,color):
    
    turtle.fillcolor(color)
    #pen is up
    turtle.penup()



    #going into position
    turtle.left(90)
    turtle.forward(height/2)
    turtle.left(90)
    #in position
    turtle.pendown()

    #filling of color has begun
    turtle.begin_fill()

    #drawing has started, half length to end up with a centered rectangle.
    turtle.forward(length/2)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length/2)
    #drawing has ended.


    turtle.end_fill()
    #done filling.

    #pen up, returning to original position.
    turtle.penup()
    turtle.right(90)
    turtle.backward(height/2)
    turtle.right(90)
    #now in original pos, conclude.

def draw_table(table_length,table_height,table_color):
    turtle.fillcolor(table_color)


    draw_rectangle(table_length,table_height,table_color)

    #taking coords for original positioning
    org_x = turtle.xcor()
    org_y = turtle.ycor()

    #pen has been lifted to go into pos
    turtle.penup()

    #going into position, not drawing
    turtle.left(90)
    turtle.forward(table_height/2)
    turtle.right(90)
    turtle.forward(table_length/2)
    turtle.right(90)
    turtle.forward(table_height)

    #pen is now down, drawing started
    turtle.pendown()

    #this starts the filling
    turtle.begin_fill() 
    
    turtle.forward(table_height*8)
    turtle.right(90)
    turtle.forward(table_length/20)
    turtle.right(90)
    turtle.forward(table_height*8)
    turtle.right(90)
    turtle.forward(table_length/20)

    #filling ended
    turtle.end_fill()


    '''
    FIRST LARGE LEG DONE, MOVING ON TO SECOND LARGE.
    '''

    #pen up
    turtle.penup()
    turtle.left(90)

    '''
    GOING BACK TO ORIGINAL POSITION!
    '''
    turtle.goto(org_x,org_y)
    turtle.setheading(0)

    #going into position, not drawing
    turtle.left(90)
    turtle.forward(table_height/2)
    turtle.left(90)
    turtle.forward(table_length/2)
    turtle.left(90)
    turtle.forward(table_height)

    #now in position, drawing begin.

    #pen down
    turtle.pendown()

    #begin fill
    turtle.begin_fill()

    turtle.forward(table_height*8)
    turtle.left(90)
    turtle.forward(table_length/20)
    turtle.left(90)
    turtle.forward(table_height*8)
    turtle.left(90)
    turtle.forward(table_length/20)


    #end fill
    turtle.end_fill()

    #drawing finished.
    

    '''
    SECOND LARGE LEG DONE.
    '''

    #pen is up.
    turtle.penup()
    turtle.right(90)
    '''
    GOING BACK TO ORIGINAL POSITION!
    '''
    turtle.goto(org_x,org_y)
    turtle.setheading(0)


    '''
    TWO SMALL LEGS BEING DRAWN
    '''


    #going into position
    turtle.forward(table_length/4)
    turtle.right(90)
    turtle.forward(table_height/2)

    
    #pen is now down, drawing started
    turtle.pendown()
    #filling begun
    turtle.begin_fill()

    turtle.forward(table_height*4)
    turtle.right(90)
    turtle.forward(table_length/18)
    turtle.right(90)
    turtle.forward(table_height*4)

    #filling done, struture drawn.
    turtle.end_fill()

    #pen is up again
    turtle.penup()


    '''
    GOING BACK TO ORIGINAL POSITION!
    '''
    turtle.goto(org_x,org_y)
    turtle.setheading(0)

    #going into position
    turtle.setheading(180)
    turtle.forward(table_length/4)
    turtle.left(90)
    turtle.forward(table_height/2)

    #pen is down, drawing start
    turtle.pendown()
    #filling begin
    turtle.begin_fill()

    turtle.forward(table_height*4)
    turtle.left(90)
    turtle.forward(table_length/18)
    turtle.left(90)
    turtle.forward(table_height*4)

    #filling done
    turtle.end_fill()

    #drawing finished
    turtle.penup()


    #final return to original position
    turtle.goto(org_x,org_y)
    turtle.setheading(90)
    turtle.forward(table_height/2)
    turtle.setheading(0)



def decor_assist(length):
    print("find a way to see if you can put the decorations equally based on each length")

screen = turtle.Screen()







def main():

    #Cake Config, config cake size and variables.
    layer_am = int(input("Select the amount of layers you'd like")) #.5
    cake_length_x = int(input("Select the cake length (X)")) #find min for all values .. 400
    cake_height_y = int(input("Select cake length (Y)"))#..30

    table_length_x = int(input("Select table length (X)")) #..500
    table_height_y = int(input("Select table length (Y)")) #.50
    table_color = input("select table color")
    

    incre_variable = float(input("Select increment variable, we suggest 1.5")) #incre variable for the loop, basically the space between each layer.

    x_start = int(input("Select X starting point."))
    y_start = int(input("Select Y starting point.")) #the start values, all inputs must be added later

    turtle.goto(x_start,y_start) #going to chosen x and y startpoints.

    turtle.speed(0)

    screen.setup(table_length_x*2,table_height_y*14)

    draw_table(table_length_x/1.2,table_height_y/1.5,table_color) #draw table
    turtle.left(90)
    turtle.forward(cake_height_y/2)
    turtle.right(90)

    #layer looping, takes each color of each layer, loops over the size.
    for i in range(int(layer_am)):
        
        #asks for the color, this keeps looping until all layers are done.
        color_layer = input(f"What color do you want for layer #{layer_am}? \n")

        #this is for decrement of variable, it reduces by a value chosen by a user, can be edited.
        cake_length_x = cake_length_x/incre_variable



        #DRAWING PROCESS BELOW

        #pen is down, drawing of rectangle started.
        turtle.pendown()
        draw_rectangle(cake_length_x,cake_height_y,color_layer)

        #pen is up, drawing over.
        turtle.penup()

        #getting x and y coordinates for movement up
        xc = turtle.xcor()
        yc = turtle.ycor()

        #moving up into new position to continue loop
        turtle.goto(xc,yc+cake_height_y)
        turtle.penup()

        #decrement of the loop itself to continue.
        layer_am = layer_am - 1


    #pen is now up
    turtle.penup()

    #going into position above the cake!
    turtle.goto(xc,yc-cake_height_y/2)
    turtle.left(90)
    turtle.forward(cake_height_y)
    #now in position to draw candle.


    candlette(cake_length_x,cake_height_y,cake_height_y/5)
    turtle.goto(xc,yc-cake_height_y/4)

    diamond_deco(table_length_x/12,table_height_y/12)



    hey = input("press")

main()







'''
ALGORITHIM FOR LOOP!
so basically, we want to create an algorithim to somehow loop multiple layers over and over.
let's assume we're using 5 layers
first layer : draws normal rectangle with original dimension, 500x100
second layer : 450x100, decrease the length.
third layer : gets smaller 325x100
fourth layer : gets smaller to 250x100
fifth layer :gets smaller to 150x100
'''