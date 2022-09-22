class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right =None

class tree:
    def creat_node(self,data):
        return Node(data)
    def insert_node(self,node,data):
        if node is None:
            return self.creat_node(data)
        if data<node.data:
            node.left = self.insert_node(node.left,data)
        else:
            node.right = self.insert_node(node.right,data)
        return node
    def is_BST(self,root):
        if root is not None:
            self.is_BST(root.left)
            B.append(root.data)
            self.is_BST(root.right)
B = []
A = [2,10,7,15,12,20,30,6,8]
T = tree()
root = T.creat_node(5)
for i in A:
    T.insert_node(root,i)
T.is_BST(root)
a =len(B)-1
for j in range(len(B)-2,-1,-1):
    if B[j]>=B[a]:
        print(False)
    a-=1
print(True)