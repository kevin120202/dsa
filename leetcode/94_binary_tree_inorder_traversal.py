class Solution(object):
    def inorderTraversal(self, root):
        res = []
        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            res.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        return res