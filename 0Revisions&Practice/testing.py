'''
import csv

def openCsv():
    with open("./data/aap.csv") as file:
        reader = csv.reader(file)

        for line in reader:
            print(line)

openCsv()
'''

