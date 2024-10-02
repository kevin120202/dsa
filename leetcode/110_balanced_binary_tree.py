# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True

        def height(node):
            if node is None:
                return 0
            
            left_h = height(node.left)
            right_h = height(node.right)
            if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
                return -1

            return 1 + max(left_h, right_h)
                
        return height(root) != -1