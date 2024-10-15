class Solution(object):
    def postorderTraversal(self, root):
        res = []
        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res