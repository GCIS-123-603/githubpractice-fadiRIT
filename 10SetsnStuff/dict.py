ThisDictionary = {"brand":"Mercedes",
                  "Model":"G63",
                  "Cost":"$250,000",
                  "Year":"2020"}

def key_checker(key):
    
    if key in ThisDictionary:
        print("True!")
    else:
        print("not there.")

key_checker("Model")




def names():

    familyNames={}

    familyNames["D"] = 'Donald'
    familyNames["M"] = "Mohamad"
    familyNames["E"] = "Elon"

    familyNames["D"] += "Trump"
    familyNames["M"] += "Waleed"
    familyNames["E"] += ""

    familyNames["D"] += "Junior"
    familyNames["M"] += "Durak"
    familyNames["E"] += "Musk"

    for key,value in familyNames.items():
        print(key,value)


def main():
    names()
main()  

if __name__ == "__main__":
    main()