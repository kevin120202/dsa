# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if root is None:
            return False
        
        if self.isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2 or tree1.val != tree2.val:
            return False
        return self.isSame(tree1.left, tree2.left) and self.isSame(tree1.right, tree2.right)