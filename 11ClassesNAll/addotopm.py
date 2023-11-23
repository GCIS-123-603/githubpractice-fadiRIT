class Addition:
    first = 0
    second = 0
    answer = 0

    #define parameter consutrctor

    def __init__(self,firstUpdateValue, secondUpdateValue):
        self.first=firstUpdateValue
        self.second=secondUpdateValue

    def add(self):
        self.answer=self.first+self.second

    def sub(self):
        self.answer=self.second-self.first
    
    def multiply(self):
        self.answer=self.first*self.second
    
    def divide(self):
        self.answer=self.second/self.first

    def display(self):
        print("First",self.first)
        print("Second",self.second)
        print("Total",self.answer)
    


object1 = Addition(100,300)
object1.add()
object1.divide()
object1.display()

object2 = Addition(500,500)
object2.add()
object2.display()