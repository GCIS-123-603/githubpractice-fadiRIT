import csv

filename = "./data/aap.csv"

fields=[]
rows=[]

#reading csv files
with open(filename) as csvfile:

    #creating csv reader
    cSv_reader = csv.reader(csvfile)

    #extracting field names from first row
    fields = next(csvfile)

    #extracting each data row 1 by 1
    #for row in cSv_reader:
        #rows.append(row)
    
    for row in cSv_reader:
        print(row)    

    print("Total number of rows",cSv_reader.line_num)
    print("Total number of columns")

    