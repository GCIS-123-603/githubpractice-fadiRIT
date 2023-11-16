import re

def find_digits(stringInput):

    for match in re.findall("[0-9]+",stringInput):
        print(match)


find_digits("01abc02def07ghi")


def check_digits():
    for match in re.findall("\d[a-z]", "1ab23c"):
        print(match)

    if re.findall("\d[a-z]","1abcdef"):
        print("At least one match found!")
    else:
        print("No match!")


#check_digits()