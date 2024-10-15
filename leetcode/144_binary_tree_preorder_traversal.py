class Solution(object):
    def preorderTraversal(self, root):
        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        return res