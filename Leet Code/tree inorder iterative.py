class Node:
    def __init__(self,val):
        self.left  =None
        self.data= val
        self.right = None
class tree:
    def creat_node(self, data):
        return Node(data)
    def insert(self, node, data):
        if node is None:
            return self.creat_node(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def traverse_inoder(self, root):
        if root is not None:
            self.traverse_inoder(root.left)
            print(root.data)
            self.traverse_inoder(root.right)
Tree = tree()
A = [2,10,7,15,20,30,6,8]
root = Tree.creat_node(5)
for i in A:
    Tree.insert(root,i)
Tree.traverse_inoder(root)


# class Node:
#     def __init__(self,info):
#         self.info  =info
#         self.left =None
#         self.right  =None
#         self.level = None
#     def __str__(self):
#         return str(self.info)
# def preorder(root):
#     if root  == None:
#         return
#     print(root.info,end="")
#     preorder(root.left)
#     preorder(root.right)
# class BinarySearchtree:
#     def __init__(self):
#         self.root  =None


# class Node:
#     def __init__(self, info):
#         self.info = info
#         self.left = None
#         self.right = None
#         self.level = None
# def preOrder(root):
#     if root == None:
#         return
#     print(root.info, end=" ")
#     preOrder(root.left)
#     preOrder(root.right)
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#     def insert(self, val):
#         if self.root is None:
#             self.root = Node(val)
#             return
#         root = self.root
#         while 1:
#             if val < root.info:
#                 if root.left is not None:
#                     root = root.left
#                 else:
#                     root.left = Node(val)
#                     break
#             elif val >= root.info:
#                 if root.right is not None:
#                     root = root.right
#                 else:
#                     root.right = Node(val)
#                     break
# tree = BinarySearchTree()
# t = int(input())
# arr = list(map(int, input().split()))
# for i in range(t):
#     tree.insert(arr[i])
# preOrder(tree.root)
