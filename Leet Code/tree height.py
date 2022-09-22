class Node:
    def __init__(self,val):
        self.left= None
        self.data = val
        self.right = None
class tree:
    def creadtnode(self,data):
        return Node(data)
    def insertnode(self,node,data):
        if node is None:
            return self.creadtnode(data)
        if data<node.data:
            node.left = self.insertnode(node.left,data)
        else:
            node.right  =self.insertnode(node.right,data)
        return node
    def hightTree(self,root):
        if root is None:
            return -1
        else:
            return max(self.hightTree(root.left),self.hightTree(root.right))+1

A = [2,10,7,15,12,20,30,6,8]
T = tree()
root = T.creadtnode(5)
for i in A: 
    T.insertnode(root,i)
print(T.hightTree(root))