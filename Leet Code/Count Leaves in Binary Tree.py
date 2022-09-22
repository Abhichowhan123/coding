def countLeaves(root):

    def count(root):

        if not root:
            return 0
        if root.left== None and  root.right==None:
            return 1
        return count(root.left)+count(root.right)
    return count(root)