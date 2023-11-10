'''
numbersd = list(range(0,21))
numbers = list(range(0,50))
print([0 for _ in range(15)])
print([char for char in 'foobar'])
print([q for q in numbersd if q%2==0])
print([q for q in numbers if q%3==0 or q%5==0])
'''


rows, cols = (3,3)
arr = [[0]*cols]*rows
print(arr)

arr[0]=[1,1,1]
print(arr)

