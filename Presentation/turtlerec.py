import turtle

turtle.setheading(0)

def circles(radius,rec_depth):
    if rec_depth==0:
        return 0
    else:

        turtle.setheading(0)
        turtle.penup()

        turtle.forward(radius)
        turtle.pendown()

        turtle.left(90)
        turtle.circle(radius)
        turtle.right(90)

        turtle.penup()
        turtle.backward(radius)

        return circles(radius/1.2,rec_depth-1)



def main():
    circles(200,10)

    take = input("Press to proceed")



main()



