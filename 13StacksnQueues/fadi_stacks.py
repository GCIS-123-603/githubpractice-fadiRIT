class Node:
    __slots__ = ["__data", "__next"]

    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, data):
        self.__data = data

    def set_next(self, next):
        self.__next = next

    def __str__(self):
        return  str(self.get_data()) + " " + str(self.get_next())

class Stack:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def get_head(self):
        return self.__head

    def get_size(self):
        return self.__size

    def set_head(self, head):
        self.__head = head

    def set_size(self, size):
        self.__size = size

    def __str__(self):
        return  str(self.get_head()) + " " +  str(self.get_size())

    ## stacking
    def push(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
        else:
            new_node.set_next(self.__head)
            self.__head = new_node
        self.__size += 1

    def pop(self):
        if self.__head is None:
            return None
        else:
            poop_data= self.__head.get_data()
            self.__head = self.__head.get_next()
            self.__size -= 1
            return poop_data



def main():
    malooka = Stack()
  
    print(malooka.get_size())

    malooka.push(10)
    malooka.push(20)
    malooka.push(30)

    print(malooka.get_size())

    malakGCISrizz = Stack()

    malakGCISrizz.push(1)
    malakGCISrizz.push(2)
    malakGCISrizz.push(3)

    print(malakGCISrizz)

    poop = malakGCISrizz.pop()
    print(poop)

    print(malakGCISrizz)
main()

