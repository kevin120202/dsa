# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


        # queue1 = [p]
        # v1 = []
        # queue2 = [q]
        # v2 = []
        # while queue1:
        #     curr = queue1.pop(0)
        #     if curr:
        #         v1.append(curr.val)
        #         if curr.left:
        #             queue1.append(curr.left)
        #         else:
        #             queue1.append(None)
        #         if curr.right:
        #             queue1.append(curr.right)
        #         else:
        #             queue1.append(None)
        #     else:
        #         v1.append(None)
        
        # while queue2:
        #     curr = queue2.pop(0)
        #     if curr:
        #         v2.append(curr.val)
        #         if curr.left:
        #             queue2.append(curr.left)
        #         else:
        #             queue2.append(None)
        #         if curr.right:
        #             queue2.append(curr.right)
        #         else:
        #             queue2.append(None)
        #     else:
        #         v2.append(None)
        
        # return v1 == v2
        