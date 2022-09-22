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


tree = Tree()
root  = tree.creat_node(5)
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)

