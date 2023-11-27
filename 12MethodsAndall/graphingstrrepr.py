class Graph:
    

    def __init__(self,xcor,ycor):
        self.xcor=xcor
        self.ycor=ycor
    
    def __repr__(self):
        #this method represents the objects formally
        return "Graph : ("+str(self.xcor)+","+str(self.ycor)+")" #f"Graph({str(self.xcor),str(self.ycor)})"
    
    def __str__(self):
        #We use this method for readible represnetation of an obkject
        return "("+str(self.xcor)+","+str(self.ycor)+")"


myinstance = Graph(5,5)

print(repr(myinstance))
print(str(myinstance))