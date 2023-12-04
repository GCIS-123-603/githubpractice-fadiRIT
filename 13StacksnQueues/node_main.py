from node import Node




node1= Node(value=10)
node2= Node(value=20)
node3= Node(value=30)

#connecting nodes
node1.set_nextNode(node2)
node2.set_nextNode(node3)

#accessing

#normal getter
print("Node1 : ",node1.get_value())
print("Node2 : ",node2.get_value())
print("Node3 : ",node3.get_value())

#get next node

#node1.node2.getvalue()
print("Next to Node1 : ",node1.get_nextNode().get_value())
print("Next to Node2 : ",node2.get_nextNode().get_value())