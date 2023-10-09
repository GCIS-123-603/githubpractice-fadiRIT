def read_file(directory):
    #file = open ("absolute path", "mode")
    with open(directory, "r") as file:
        read_lines = file.readlines()
        return read_lines
    
def write_file(directory):

    with open(directory,"w") as file:
        writing = file.write(input("What would you like to enter?\n"))
        return writing

def read_file_ErrorHandling(direc):

    try:
        with open(direc,"r") as file:
            reading = file.readlines()
            return reading
    
    except FileNotFoundError:
        print("The file has not been found.")

def zerodivisonerror():

    try:
        num1 = int(input("Enter your first number!"))
        num2 = int(input("Enter your second number!"))

        divTotal = num1/num2
        print(divTotal)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    
        




def main():
    #write_file("./data/hello.txt")
    #file_content = read_file("./data/hello.txt")
    #print(f"Your file content shows {file_content}"
    #read_file_ErrorHandling("./wsp.txt")
    
    zerodivisonerror()
main()