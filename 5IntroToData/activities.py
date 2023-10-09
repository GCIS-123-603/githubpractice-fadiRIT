



def numbers():

    number_of_files = int(input("How many files would you like to enter?"))

    i = 0
    while i <= number_of_files:
        file_name = str(input("Enter the file name/directory!"))

        with open(file_name) as file:
            read_file = file.readlines()  
            
            for i in range(3):
                pass


            
        
    i=i+1
            
def numbers_test():
    number_of_files = 1

    i = 0

    while i <= number_of_files:
        file_name="./data/numbers_01.txt"

        with open(file_name) as file:
            read_lines = file.readlines()
            






def main():
    #numbers()
    numbers_test()


main()