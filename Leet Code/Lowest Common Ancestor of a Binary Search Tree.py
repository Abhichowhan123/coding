root = [6,2,8,0,4,7,9,3,5]
p = 2
q = 8
class Node:
    def __init__(self,val):
        self.left  =None
        self.data  =val
        self.right = None
class Tree:
    def creadt_node(self,data):
        return Node(data)
    def insert_node(self,node,data):
        if node is None:
            return self.creadt_node(data)
        if data<node.data:
            node.left = self.insert_node(node.left,data)
        else:
            node.right= self.insert_node(node.right,data)
        return node
    
t = Tree()
r = t.creadt_node(root[0])
for i in range(len(root)-1):
    t.insert_node(r,root[i+1])
