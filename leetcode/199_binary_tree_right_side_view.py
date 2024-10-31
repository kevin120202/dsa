# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        res = []
        q = [root]

        while q:
            right = None
            q_len = len(q)

            for i in range(q_len):
                node = q.pop(0)
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
            
            if right:
                res.append(right.val)
        
        return res