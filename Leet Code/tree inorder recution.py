class Node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None
class Tree:
    def creat_node(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.creat_node(data)
        if data<node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node
    def inoder(self,root):
        if root is not None:
            self.inoder(root.left)
            print(root.data,end=" ")
            self.inoder(root.right)
    def preorder(self,root):
        if root is not None:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
tree = Tree()
root  = tree.creat_node(5)
A = [2,10,7,15,20,30,6,8]
for i in A:
    tree.insert(root,i)
print("inoder")
tree.inoder(root)
print()
print("preorder")
tree.postorder(root)
print()
print("postorder")
tree.preorder(root)