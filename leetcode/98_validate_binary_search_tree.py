# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):

        def isValid(root, lower, upper):
            if not root:
                return True
            
            if root.val <= lower or root.val >= upper:
                return False
            
            return (isValid(root.left, lower, root.val) and
                isValid(root.right, root.val, upper))

        return isValid(root, float("-inf"), float("inf"))