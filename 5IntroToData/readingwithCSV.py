import csv

def read_csv_file():
    with open("./data/grades_010.csv","r") as sample_csv:
        reader = csv.reader(sample_csv)
        
        next(reader)

        for line in reader:
            print(f"Final Exam Grades for {line[0]} : {line[4]}")

def average_calculatable():
    with open("./data/averages.csv") as csv_file:
        reader = csv.reader(csv_file)

        lines = []

        for line in csv_file:
            stripped = line.strip() #removing any white spaces or of that sort.
            stripped= stripped.split(',') #splitting based on comma.

            #stripped is still a string! convert to float.
            line_sum = sum(float(i) for i in stripped)
            lines.append(line_sum/len(stripped))
            print(stripped)

            return lines


    