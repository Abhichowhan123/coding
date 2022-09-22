class Node:
    def __init__(self,val):
        self.left = None
        self.data  =val
        self.right = None
class tree:
    def createnode(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.createnode(data)
        if node.data>data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
Tree = tree()
A = [2,10,7,15,20,30,6,8]
root = Tree.createnode(5)
for i in A:
    Tree.insert(root,i)
Tree.postorder(root)

