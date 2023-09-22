import turtle
import random

def draw_rectangle(length,height,color):


    #pen is up
    turtle.penup()
    #moving into position
    turtle.fillcolor(color)
    turtle.left(90)
    turtle.forward(height/2)
    turtle.left(90)

    #pen is down, in position.
    turtle.pendown()

    #drawing shape begins, working via proportions and inputs.
    turtle.begin_fill()
    turtle.forward(length/2)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length/2)
    turtle.end_fill()

    turtle.penup()
    #pen up,done drawing, going back to original position
    turtle.right(90)
    turtle.backward(height/2)
    turtle.right(90)

def inputs_forlate():
         #Env Variables. configures env.
    #screen_size_x = int(input("Please input the desired screensize! (X)\n"))
    #screen_size_y = int(input("Please input the desired screensize (Y)!\n"))
    #world_coords_x = int(input("Pick your world coordinates! (X)\n"))
    #world_coords_y = int(input("Pick your world coordinates! (y)\n"))
    turtle_speed = int(input("Select your turle speed!\n"))

    #Table Config, picks table sizes.
    #table_color = (input("Select the color of your table!\n"))
    #table_x = int(input("Select the length (X) of your table\n"))
    #table_y = int(input("Select the height (Y) of your table\n"))

    #Cake Config, config cake size and variables.
    layer_am = int(input("Enter the amount of layers you'd like on your cake!\n"))
    length_cake_x = int(input("Please enter the length (x) of the cake!\n"))
    height_cake_y = int(input("Please enter the height (y) of the cake!\n"))
    #radius_r = int(input("Please enter the radius!\n"))
    #decoration_cake = int(input("Please select a number for decoration from the following:\n1. Stars\n2. HBD\n3. YAY! \n"))

    #Position Config, configs starting position.
    start_position_x = int(input("Pick your starting position! X\n"))
    start_position_y = int(input("Pick your starting position! Y\n"))


    turtle.goto(start_position_x,start_position_y)
    turtle.speed(turtle_speed)

def calculate_for_loop():
   xc = turtle.xcor()
   yc = turtle.ycor()



#The main function, which executes the whole program.
def main():
    turtle_speed = int(input("Select your turle speed!\n"))

    #Cake Config, config cake size and variables.
    layer_am = int(input("Enter the amount of layers you'd like on your cake!\n"))
    length_cake_x = int(input("Please enter the length (x) of the cake!\n"))
    height_cake_y = int(input("Please enter the height (y) of the cake!\n"))

    #Position Config, configs starting position.
    start_position_x = int(input("Pick your starting position! X\n"))
    start_position_y = int(input("Pick your starting position! Y\n"))


    turtle.goto(start_position_x,start_position_y)
    turtle.speed(turtle_speed)
    for i in range(layer_am):
        draw_rectangle(length_cake_x-layer_am*2,height_cake_y,"red")
        layer_am = layer_am - 1

    '''
    so basically, we want to create an algorithim to somehow loop multiple layers over and over.
    let's assume we're using 5 layers
    first layer : draws normal rectangle with original dimension, 500x100
    second layer : 450x100, decrease the length.
    third layer : gets smaller 325x100
    fourth layer : gets smaller to 250x100
    fifth layer :gets smaller to 150x100
    '''




    proceed = input("Press anything to proceed!")

main()