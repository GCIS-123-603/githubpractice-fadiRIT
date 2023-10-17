

def openFile():
    with open("./Filatives/drawing04.txt") as turtleDrawing:

        readlines = turtleDrawing.readlines()

        for i in readlines:
            
            for char in i:
                list_color.append(char)


list_color = []
        

def drawPixBlack():
    print("drawing black pixel!")

def drawPixWhite():
    print("drawnig white pix!")

openFile()
print(list_color)
