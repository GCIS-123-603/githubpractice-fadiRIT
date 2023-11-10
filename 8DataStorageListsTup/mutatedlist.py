
def make_list(a_sequence):
    created = []


    for data in a_sequence:
        created.append(data)


    print(created)

def scale(a_list,scalar):
    #loop over list and modif yvalue by multiplgin
    created = []


    for data in a_list:
        created.append(data*scalar)


    print(created)

    pass

def main():

    ListedList = [1,45,12,4,5678,9]



    #make_list(ListedList)
    scale(ListedList,4)




main()