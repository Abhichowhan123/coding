class Node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None
class Tree:
    def createNode(self,data):
        return Node(data)
    def insertNode(self,node,data):
        if node is None:
            return self.createNode(data)
        if data<node.data:
            node.left = self.insertNode(node.left,data)
        else:
            node.right= self.insertNode(node.right,data)
        return node

    def preorder(self,root):
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
T = Tree()
A = [2,10,7,15,20,30,6,8]
root = T.createNode(5)
for i in A:
    T.insertNode(root,i)
T.preorder(root)