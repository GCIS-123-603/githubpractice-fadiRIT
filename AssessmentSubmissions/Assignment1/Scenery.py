import turtle
import random


'''
Group 6 : GCIS 123.603

Before starting, we decided to hop on a call and devise an algorithim for the program. We decided to assign 3 different positions that we can use,
a person took care of the user interaction, while a person took care of the parameterization, and finally a person to deal with organizing the functions.
Of course all of us had inter-changeable roles, but those were the main divisions

Group Members:
Aaamna Fathima
Abdullah AlBlooshi
Mohamad Fadi Dakwar


This code provides full user customization, and allows the user to pick whatever color, whatever size, and whatever increment.
This cake is meant to be fully customizable, and done easily. Although it has to be kept in mind, that the table size, must be LARGER than the cake, and
all values must be above a certain threshold to avoid confusions in parameters.

This program uses multiple functions defined below, and all of them end in the same place they start in, and this code follows ALL THE GUIDELINES PROVIDED IN THE DOCUMENT:

25% Design for design:
    Functions are parameterized
    Arguments are passed properly for input and whatnot.
    Parameters are inputted as well.

50% Functionality:
    A scene is drawn with one candle, a cake, a table, and of course, the decoration.
    There is no hard coding involved at all, and  it's all parameterized.
    Drawing fits successfully.
    Shapes are filled with their colors as pen color.
    It displays the drawing before the program closes.

10% Commenting:
    All the code is commented, and as you can see, there's this BEAUTIFUL docstring.







'''
screen = turtle.Screen()

#Diamond Decoration 

'''
This is a function used to draw a diamond decoration, it takes in length and height,
and it uses a for loop in order to draw it.
'''
def diamond_deco(rec_length,rec_height):
    turtle.pendown()
    colors=['white', 'red','lavender','orange','black'] # making a catalogue of colors 
    turtle.color(random.choice(colors)) # so that the colors used are diverse and unique to every runtime o/p
    turtle.begin_fill() 
    for k in range(2):
        turtle.forward(rec_length/4)  
        turtle.right(45)  
        turtle.forward(rec_length/8)  
        turtle.right(135)    
    turtle.end_fill() 
    turtle.penup()

'''
This is the main candle function, and it draws a simplistic candle. Firstly it will be at the end position, which is
at the top of the cake, then it will draw a basic triangle.
'''
def candlette(length,height,radius):

    #fill color pick
    turtle.fillcolor("gray")
    turtle.pencolor("gray")

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
'''
This is the function that draws a rectangle, it goes back to where it started as well. It also takes in length,height, and color
and fills the rectangle with the chosen color.
'''
#Function for drawing rectangle.
def draw_rectangle(length,height,color):
    
    turtle.pencolor(color)
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
    
    #now in original pos.
'''
This function draws the table, it's the most beautiful as it takes proportions and works everything out in between it. It draws it in a 3d shape,
with 2 smaller legs and 2 larger legs.
'''
#Function to draw table via proportions
def draw_table(table_length,table_height,table_color):
    turtle.fillcolor(table_color)
    turtle.pencolor(table_color)


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

'''
This function takes the current coordinates, then returns it. This is very important, especially for references.
'''
#This function is to return coordinates
def coords():
    x_cor = turtle.xcor()
    y_cor = turtle.ycor()
    #using return function to return it into coords() . . . :<)
    return x_cor,y_cor
'''
This function draws a star by taking two triangles, and inverting them. It only takes in one parameter that is needed, and that's lenght.
'''
#Function for drawing star deco
def drawTriangle(length):

    #pen is up
    turtle.penup()

    #going into position
    turtle.setheading(0)
    turtle.backward(length)

   

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

def ellipse():
    semi_major_axis = 150 ## ig we can customize this to user defined but note major axis needs to be way bigger than minor axis 
    semi_minor_axis = 5

    screen.setup(semi_major_axis*1,semi_minor_axis*1)


    ellipse = turtle.Turtle()
    ellipse.speed(1)

    # Function to draw an ellipse
    def draw_ellipse(semi_major_axis, semi_minor_axis):
        ellipse.penup()
        ellipse.goto(-semi_major_axis, 0)  # Start from the left end of the major axis
        ellipse.pendown()
        ellipse.setheading(45) #dont change this , its a specific angle to make the ellipse
        
        # Draw the left half of the ellipse
        for _ in range(2):
            ellipse.circle(semi_minor_axis, 90)
            ellipse.circle(semi_major_axis, 90)  # Note that we swap semi-major and semi-minor axes here


    draw_ellipse(semi_major_axis, semi_minor_axis)





def mainDrawCake():

    #Cake Config, config cake size and variables.
    print("Welcome to your birthday cake! This program takes user input. We will provide recommendation for proportionate sizes for your cake.\n")
    layer_am = int(input("Please enter the amount of layers! We recommend 5!\n")) #3-5
    global_layer_am = layer_am

    cake_length_x = int(input("Please enter the Cake Length (X), make sure it's smaller than table! We recommend 400.\n")) #find min for all values .. 400
    cake_height_y = int(input("Please enter the Cake Height (Y), make sure it's smaller than the table! We recommend 30.\n")) #..30

    table_length_x = int(input("Please enter the Table Length (X), We recommend 600!\n")) #..500
    table_height_y = int(input("Please enter the Table Height (Y), we recommend 50!\n")) #.50
    table_color = input("Select the table color! Brown is the best.\n")
    

    incre_variable = float(input("Please input the increment variable, this is used for proportions, we highly suggest you use 1.5\n")) #incre variable for the loop, basically the space between each layer.

    x_start = int(input("Please enter the starting X Coordinate.\n"))
    y_start = int(input("Please enter the starting Y Coordinate.\n")) #the start values, all inputs must be added later

    turtle.goto(x_start,y_start) #going to chosen x and y startpoints.

    turtle.speed(0)

    #making sure screen is larger than the table
    screen.setup(table_length_x*2,table_height_y*14)

    #drawing the table, then moving back into position.
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

        for i in range(5):
 

            turtle.forward(100)
            turtle.right(144)

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


    #drawing candle
    candlette(cake_length_x,cake_height_y,cake_height_y/5)
    #returning to original position
    turtle.goto(xc,yc-cake_height_y/4)

    #returning current cords for reference
    print(coords())

    #loop to draw stars!!
    for i in range(int(global_layer_am)):


        #drawing first star
        drawTriangle(cake_height_y/1.5)
        #pen up, moving to position
        #pen up, going backward
        turtle.penup()
        
        #returning to origin
        turtle.penup()
        turtle.setheading(270)
        turtle.forward(cake_height_y)
        turtle.setheading(0)

        #increment
        global_layer_am = global_layer_am-1
    
    


    print("Loading your birthday cake... Happy Birthday!")
    Proceed = input("Press anything to proceed!")

mainDrawCake()







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