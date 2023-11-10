
def tuples(a_tuple):
    print(len(a_tuple))

    print(a_tuple)

    for i in a_tuple:
        print(i)

def lists(a_list):

    for i in a_list:
        print(i)
    


def main():
    jungle = (1,2,3,"hey",True,None,"whot?")
    listedlist = [34,1,57,True,"hey",'wyd',541,None]


    print("TUPLE START\n")

    tuples(jungle)


    #jungle[1] = "changed.."
    #tuples(jungle)

    print("\nTUPLE ENDED, LIST BEGIN.\n")

    lists(listedlist)

    print("\nLIST ENDED.\n")


main()