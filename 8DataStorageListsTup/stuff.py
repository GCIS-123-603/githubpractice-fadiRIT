import random

'''
def tuples():
    nums = tuple(random.random() for i in range(3))
    return nums

def main():
    print(tuples())

main()

'''

def rgb_tuple():
    red = random.random()
    green = random.random()
    blue = random.random()

    return (red,green,blue)

def tuple_equality(tupleA,tupleB):

    print("\nThis is the tuple 9: \n",tupleA,tupleB)

    if tupleA==tupleB:
        print("== Operator states True!")

    if tupleA is tupleB:
        print("IS operator states True!")
        
    
def main():
    rgb_randoms = rgb_tuple()



    CreatedList = ['a',1,'2']
    reverseList = ['2',1,'a']

    tupledCreatedList = tuple(CreatedList)
    reverseTupleList = tuple(reverseList)

    tuple_equality(tupledCreatedList,tupledCreatedList)
    tuple_equality(tupledCreatedList,reverseTupleList)

    


main()