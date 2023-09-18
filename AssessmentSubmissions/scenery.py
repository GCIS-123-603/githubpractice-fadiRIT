import turtle

# PROGRAM BRIEF!
'''

Today we're gonna be making a program using turtle module, which will draw scene with :
1 CANDLE, 1 TABLE, 1 CAKE, 1 DECORATION.

The program is designed to be flexible, and allow the user to pick parameters.

Function must use return values, NO HARD CODING.
Drawing must fit, BORDER LINES MUST FIT FILL COLORS.
Has to be viewed and triggered to be closed.

Birthdaycake, with candle on top of the cake, with the whole cake on a table. Layout free for choice.
It MUST take input for color, table size, cake size, cake must be on table.

This must have reusable functions, table drawing function, cake drawing function made of smalelr functions.

The main functions of the program include:
1. draw_rectangle(length,height,color) - this draws a rectangle.
2. candle() - which draws a candle with a fire on it.
3. inputs() - A function which will collect all the inputs and store them in variables.
4. main() - the main drawing function of the whole scene, contains everything organized in it.

the program has to wait for the user to press a button in order to close.

'''
turtle.shape("turtle")




def draw_rectangle(length,height,color):

    #pen is up
    turtle.penup()
    #moving into position
    turtle.fillcolor(color)
    turtle.left(90)
    turtle.forward(height/2)
    turtle.left(90)

    #now in position
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

def candle(): #comes after cake_base func
    #pen is still up
    turtle.speed(1) 
    turtle.color('purple')
    
    #moving into position
    turtle.left(90)
    turtle.forward(30)
    turtle.pendown() 

    #taking the length as 10 and breadth as 100
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()

    #flame 
    #pen is down
    #moving into position
    turtle.speed(1)
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)

    #in position

    turtle.pensize(1)
    turtle.color('orange')
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.forward(100)

#This is the inputs function, it contains all inputs.
def inputs():
    #Env Variables. configures env.
    screen_size_x = int(input("Please input the desired screensize! (X)\n"))
    screen_size_y = int(input("Please input the desired screensize (Y)!\n"))
    world_coords_x = int(input("Pick your world coordinates! (X)\n"))
    world_coords_y = int(input("Pick your world coordinates! (y)\n"))

    #Table Config, picks table sizes.
    table_color = (input("Select the color of your table!\n"))
    table_x = int(input("Select the length (X) of your table\n"))
    table_y = int(input("Select the height (Y) of your table\n"))

    #Cake Config, config cake size and variables.
    layer_am = int(input("Enter the amount of layers you'd like on your cake!\n"))
    length_cake_x = int(input("Please enter the length (x) of the cake!\n"))
    height_cake_y = int(input("Please enter the height (y) of the cake!\n"))
    radius_r = int(input("Please enter the radius!\n"))
    decoration_cake = int(input("Please select a number for decoration from the following:\n1. Stars\n2. HBD\n3. YAY! \n"))

    #Position Config, configs starting position.
    start_position_x = int(input("Pick your starting position! X\n"))
    start_position_y = int(input("Pick your starting position! Y\n"))

    turtle.goto(start_position_x,start_position_y)



#Main function, draws the whole scene, with multiple functions inside of it.
def main():
    #inputs()
    turtle.goto(0,0)
    turtle.speed(3)

    draw_rectangle(500,100,"green")
    candle()





    proceed = input("Press anything to proceed!")

main()


#Questions to ask
'''
1. How are we gonna use return functions in this program?

2. How are we gonna make the table ? Proportions, 4 legs etc..

3. How are we gonna make the cake layers, and their colorations and sizes.


'''