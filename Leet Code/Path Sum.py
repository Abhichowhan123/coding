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

    def path(self,root,target):
        if not root:
            return False
        target -= root.data
        if not root.left and root.right and target==0:
            print(True)
            return

        return self.path(root.left,target)or self.path(root.right, target)

Tree = tree()
target = 31
A = [2,10,7,15,20,30,6,8]
root = Tree.creat_node(5)
for i in A:
    Tree.insert(root,i)
Tree.path(root,target)

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#