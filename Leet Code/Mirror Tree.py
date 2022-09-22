class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        temp = root.left
        root.left = root.right
        root.right = temp

        mirror(root.left)
        mirror(root.right)
