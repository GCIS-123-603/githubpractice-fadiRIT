

#firstly, we declare an array.

array = [23,32,10,20,60]

for i in range(0,len(array)):
    print(array[i], end=" ") #to append and make it on one line, rather than multiple new lines.

array.append(99) #append means add an element/value to the array

array[0] = 100
print(array)