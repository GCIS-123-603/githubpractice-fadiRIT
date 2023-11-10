import array as arr

def making_arrays():
    array1 = arr.array("i",[10,20,30,40,50])

    index = 0
    while index<len(array1):
        print(array1[index])
        index = index+1





def main():
    making_arrays()

main()