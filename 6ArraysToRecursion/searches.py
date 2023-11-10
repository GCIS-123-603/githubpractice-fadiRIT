import array as arr
import arrayutils as util
import time



def linear_search(arr,targ):


    for i in range(len(arr)):
        if arr[i]==targ:
            return i

    return -1

def main():

    arrayS = [10,20,30,40,50,100,200]
    target = 100

    begin = time.perf_counter()

    var = linear_search(arrayS,target)
    print(var)

    end = time.perf_counter()

    elapsed = end - begin
    print(elapsed)


main()


