class Queue:

    def __init__(self):
        self.people=[]

    def is_empty(self):
        return len(self.people)==0
    def size(self):
        return len(self.people)
    

    def enqueue(self,person):
        self.people.append(person)
    def dequeue(self):
        self.people.pop()



def main():
    QueuedMy = Queue()
    QueuedMy.enqueue("Fadi")
    QueuedMy.enqueue("Mohamad")
    QueuedMy.enqueue("Ahmad")

    print(QueuedMy.size())

main()