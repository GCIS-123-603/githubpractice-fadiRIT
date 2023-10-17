import re



def find_digits(stringInput):

    for match in re.findall("[0-9]+",stringInput):
        print(match)

string = "01abc02def03ghi"

#find_digits(string)


def check_digits():
    for match in re.findall("\d[a-z]", "1ab23c"):
        print(match)

    if re.findall("\d[a-z]","1abcdef"):
        print("At least one match found!")
    else:
        print("No match!")


check_digits()