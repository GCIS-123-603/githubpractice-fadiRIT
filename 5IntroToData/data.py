
my_filature = open("data/datum.txt")


def print_lines(file_name):
    nameFile =  open(file_name)

    for line in nameFile:
        length = len(line)
        print(length)


def main():

    print_lines("data/datum.txt")
    
main()