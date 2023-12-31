def addition_func():
    while input() != "q":
        try:
            x = int(input("Enter your first number!\n"))
            y = int(input("Enter your second number!\n"))

            if x or y == "q":
                break

            sum = x+y
            print(f"\nYour total is : {sum}")
        except:
            print("Error! Invalid Integer!")
        

    print("exited.")

def opening_file():

    try:
        with open("new.txt") as files:
            try:
                files.readline()
            except:
                print("File is not found.   ")
    except FileNotFoundError:
        print("There's a problem with accessing the file.")

def guessing_game():

    number = input("Pick a number:")
    number = int(number)

    if number < 1 or number > 10:
        raise ValueError("Invalid Guess!")
    print("You picked:",number)

guessing_game()