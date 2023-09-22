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

def diamond_deco():
    turtle.pendown()
    colors=['white', 'red','lavender','orange','black'] # making a catalogue of colors 
    turtle.color(random.choice(colors)) # so that the colors used are diverse and unique to every runtime o/p
    turtle.begin_fill() 
    for k in range(2):
        turtle.forward(15)  
        turtle.right(45)  
        turtle.forward(10)  
        turtle.right(135)    
    turtle.end_fill() 
    turtle.penup()

def candle(): #comes after cake_base func
    #pen is still up
    turtle.speed(15) 
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
    
    #moving into position
    turtle.speed(7)
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)

    #in position

    turtle.pensize(1)
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    
    #adding sparkles
    
    turtle.penup()  # pen up

    #bringing to position for 1st diamond deco
    turtle.goto(x,y) # (x,y) are at the base of candle
    
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(5)

    #in position
    diamond_deco() #to draw a 1st diamond on first layer on right side of candle
    
    #bringing to position for 2nd diamond deco 
    #pen is up
    turtle.goto(x,y)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(5)
    
    #in position
    diamond_deco() #to draw 2nd diamond on first layer on left side of candle 

    #moving to second layer , and this layer will have 3 sparkles
   
    turtle.goto(x,y) #going back to base of candle position 
    turtle.forward(43) # middle diamond , in second layer
    x2=turtle.xcor() #x coordinate on 2nd layer in middle 
    y2=turtle.ycor() #y coordinate on 2nd layer in middle
    diamond_deco() # 1st diamond , in the middle of second layer
    turtle.left(90)
    turtle.forward(70) 
    turtle.right(90) # in position for 2nd diamond , in 2nd layer , on right side
    diamond_deco() # 2nd diamond , in right side of 2nd layer 

    turtle.goto(x2,y2) # going to middle position on 2nd layer 
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90) # in position for 3rd diamond on 2nd layer
    diamond_deco() #3rd diamond , on 2nd layer , on left side 


    
    #moving to 3rd layer  , gonna have 7 diamonds
    
    turtle.goto(x2,y2) #going back to middle of 2nd layer 
    turtle.forward(43) # middle diamond , in 3rd layer
    x3=turtle.xcor() #x coordinate on 3rd layer in middle 
    y3=turtle.ycor() #y coordinate on 3rd layer in middle
    diamond_deco() # 1st diamond , in the middle of third layer
    
    turtle.left(90)
    turtle.forward(70) 
    turtle.right(90) # in position for 2nd diamond , in 3rd layer , 1st one on right side
    diamond_deco() # 2nd diamond , 1st on right side of 3rd layer 
    
    turtle.left(90)
    turtle.forward(60)
    turtle.left(270)
    diamond_deco() # 3rd diamond , 2nd on right side of 3rd layer

    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    diamond_deco() # 4th diamond , 3rd on right side of 3rd layer

    turtle.goto(x3,y3) # go to middle of 3rd layer to start on left side 

    turtle.right(90)
    turtle.forward(70)
    turtle.left(90) # in position for 3rd diamond on 3rd layer , 1st on left side
    diamond_deco() #5th diamond , on 3rd layer , 1st on left side

    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    diamond_deco() #6th diamond , on 3rd layer , 2nd on left side

    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    diamond_deco() #7th diamond , on 3rd layer , 3rd on left side

    #moving to 4th layer, drawing 7 diamonds

    turtle.goto(x3,y3) #going back to middle of 3rd layer 
    turtle.forward(70) # middle diamond , in 4th layer
    x4=turtle.xcor() #x coordinate on 4th layer in middle 
    y4=turtle.ycor() #y coordinate on 4th layer in middle
    diamond_deco() # 1st diamond , in the middle of fourth layer
    
    turtle.left(90)
    turtle.forward(70) 
    turtle.right(90) # in position for 2nd diamond , in 4th layer , 1st one on right side
    diamond_deco() # 2nd diamond , 1st on right side of 4th layer 
    
    turtle.left(90)
    turtle.forward(60)
    turtle.left(270)
    diamond_deco() # 3rd diamond , 2nd on right side of 4th layer

    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    diamond_deco() # 4th diamond , 3rd on right side of 4th layer

    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    diamond_deco() #5th diamond , 4th on right side of 4th layer


    turtle.goto(x4,y4) # go to middle of 4th layer to start on left side 

    turtle.right(90)
    turtle.forward(70)
    turtle.left(90) 
    diamond_deco() #6th diamond , on 4th layer , 1st on left side

    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    diamond_deco() #a7th diamond , on 4th layer , 2nd on left side

    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    diamond_deco() #8th diamond , on 4th layer , 3rd on left side

    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    diamond_deco() #9th diamond , on 4th layer , 4th on left side

    #just to move the stylus away
    turtle.penup()
    turtle.forward (100)


#The main function, which executes the whole program.
def main():
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
    turtle.goto(0,0)
    turtle.speed(3)

    
    draw_rectangle(500,100,"green")
    candle()





    proceed = input("Press anything to proceed!")

main()