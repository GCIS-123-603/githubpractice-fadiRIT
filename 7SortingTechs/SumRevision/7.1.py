#Insertion sort basically splits something into two parts, sorted and unsorted.
#it takes each number from the unsorted part and compares it to left, for example:
#[6,4,1,5]
#it will split into something like 6 | 4,1,5
#furthermore, itll take each one inside and comprae, for example:
# 6,4 | 1,5
# 4,6 | 1,5
# 4,6,1 | 5
# 4,1,6 | 5
# 1,4,6 | 5
# and so on.




arrayed = [1,2,3,4,5,6]
def swap(an_array,ind1,ind2):
    ind3 = an_array[ind2]#temp var, 0 == 0

    an_array[ind2]=an_array[ind1] # 4 = 0
    an_array[ind1]=ind3 # 0 = 4

    print(arrayed)

def shift(an_array,idx):
    pass


def main():
    swap(arrayed,0,4)


main()
