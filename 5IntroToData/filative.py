import csv as csv

def printLines():
    my_file = open("./data/input.txt")

    for line in my_file:
        
        strippedtext = line.strip()
        
        print(strippedtext)
    my_file.close()

def stripTest():
    example_line = " Hello!\n"
    print(example_line)

    stripped = example_line.strip()
    print(stripped)

def wordSearch(filedirec):
    wordInput = input("What is the word you'd like to search for?\n")

    file = open("./data/input.txt")
    lines = file.readlines()

    for row in lines:
        if row.find(wordInput) != -1: #if word is not equal to not there or if word is not equal to absent, it means its present. -1 IN PROGRAMMING MEANS ABSENT. that means if the word is NOT equal to absent, that means its present
            print("\nFound the word!")
            print("Line",lines.index(row))
        else:
            print("Not found")

    file.close()

def splutTest():
    stringed="Hello World"
    split_string = stringed.split(" ")
    print(split_string)

def longestWord():
    originalString = "hello my beautiful friend or perhaps verymuchaudacious"
    splittedString = originalString.split(" ")

    longest_word = ""
    
    for word in splittedString:
        if len(word)>len(longest_word):
            longest_word=word
    print("The longest word is",longest_word)

def longestWords():
    opened_file = open("./data/input.txt")
    lines = opened_file.readlines()

    longest_word = ""
    
    for line in lines:
        for word in line.split():
            if len(word)>len(longest_word):
                longest_word = word
    print("the longest word is", longest_word)
    '''
    this is a bit of a complicated program, sort of
    its going to initilize as "0" as longest_word
    then the first for loop, for line in lines, will firstly go through each line
    then the second for loop, for word in line.split(), will go through each word, and will split the previous lines.
    then it will have each word and it will compare each word to the length of longest_word which is intilized as "0", because empty
    it will redo over and over.
    
    '''
    opened_file.close()

def printNames(filename):
    openedfile = open(filename)
    lines = openedfile.readlines()
    
    print(lines)

    openedfile.close()

def readCSV():
    openedfile = open("./data/grades_010.csv")
    readCSVLine = csv.reader(openedfile)
    next(readCSVLine)

    for line in readCSVLine:
        print(line)
    
    openedfile.close()

def writeFile():
    name = input("Enter the name\n")
    a_file = open("./data/evenmore.txt","w")

    a_file.write("Hello, ")
    a_file.write(name)
    a_file.write("!")
    a_file.write("\n")

    a_file.close()

def writefileLines():
    lines = int(input("How many lines would you like to enter?\n"))
    a_file = open("./data/Lines.txt","w")
    
    for i in range(lines):
        linestoWrite = input(f"Enter line #{i}\n")
        a_file.write(linestoWrite)
        a_file.write("\n")
    
    a_file.close()

def openCSVColumn(name,column):
    with open(name) as file:
        for line in file:
            Stripped = line.strip()
            print(Stripped)

    
def main():
    #printLines()
    #stripTest()
    #wordSearch("data/input.txt")
    #splutTest()
    #longestWord()
    #longestWords()
    #readCSV()
    #writeFile()
    writefileLines()
    #openCSVColumn("./data/grades_010.csv",5)



main()