import csv

def opener(filename):

    try:
        with open(filename) as file:
            return True
  
    except IOError:
        print("Error!")
        return False
    
def main():
    inputfilename = input("Enter the filename/directory! \n")

    print("Gathering Data...\n")

    opener(inputfilename)






main()  