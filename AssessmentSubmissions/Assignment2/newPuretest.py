import turtle



def draw_pixel(color):
    turtle.fillcolor(color)

    turtle.begin_fill()
    for i in range(4):
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()

#0
def black_Pixel():
    draw_pixel("black")

#1
def white_Pixel():
    draw_pixel("white")

#2
def red_Pixel():
    draw_pixel("red")

#3
def yellow_Pixel():
    draw_pixel("yellow")

#4
def orange_Pixel():
    draw_pixel("orange")

#5
def green_Pixel():
    draw_pixel("green")

#6
def greenYel_Pixel():
    draw_pixel("yellowgreen")

#7
def sienna_Pixel():
    draw_pixel("sienna")

#8
def tan_Pixel():
    draw_pixel("tan")

#9
def gray_Pixel():
    draw_pixel("gray")

#A
def darkgray_pixel():
    draw_pixel("darkgray")

the_list = []

def main():

    inputStuff = input("Input your string to be drawn! \n")
    
    print(f"This is inputstuff {inputStuff}")

    splittedStuff = inputStuff.split() 
    print(f"This is splitted {splittedStuff}")

    for x in splittedStuff:
        print(f"this is more {x}")
    
        

if __name__ == "__main__":
    main()