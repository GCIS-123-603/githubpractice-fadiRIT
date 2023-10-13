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
    
def raise_check():

    try:
        roll = int(input("Enter your random number.\n"))

        if roll<=0:
            raise ValueError
    except ValueError:
        print("You entered an invalid number, ValueError!")

user_id = "Hey"
original_password = "Hello"

def validate(id,pas):
    fullid = id
    fullpass = pas

    if fullid ==user_id and fullpass == original_password:
        print("Welcome, user.")
        return True
    else:
        print("Wrong Entry!")
        return False
    

def login():
    attempts = 4
    while True:
        userid = input("Enter User ID:\n")
        passwd = input("Enter Password:\n")

        try:
            validate(userid,passwd)
        except ValueError as ve:
            attempts = attempts-1
            if attempts>0:
                print("Invalid", attempts,"attempting remaining.")
            else:
                raise 





def main():
    #write_file("./data/hello.txt")
    #file_content = read_file("./data/hello.txt")
    #print(f"Your file content shows {file_content}"
    #read_file_ErrorHandling("./wsp.txt")
    #zerodivisonerror()
    #raise_check()
    
    login()
main()